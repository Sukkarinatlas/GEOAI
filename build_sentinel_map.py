"""
Build sentinel.html : Sentinel-2 median, cloud-masked composite of Thailand
for the year 2026, on a Google Satellite basemap (Leaflet).

Cloud masking uses the modern Cloud Score+ dataset (recommended by Google EE).
Run AFTER authenticating:  python -c "import ee; ee.Authenticate()"
"""
import io
import ee

PROJECT = "innotech-373702"
START = "2026-01-01"
END = "2026-12-31"
CLEAR_THRESHOLD = 0.60          # Cloud Score+ : keep pixels >= this (0..1)
OUT = "sentinel.html"

ee.Initialize(project=PROJECT)
print("EE initialized on project:", PROJECT)

# --- Region: Thailand national boundary (FAO GAUL, lightweight) ---
roi = (ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level0")
       .filter(ee.Filter.eq("ADM0_NAME", "Thailand"))
       .geometry())

# --- Sentinel-2 SR + Cloud Score+ ---
s2 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
csp = ee.ImageCollection("GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED")
QA = "cs"

filtered = (s2
            .filterBounds(roi)
            .filterDate(START, END)
            .linkCollection(csp, [QA]))

n_scenes = filtered.size().getInfo()
print(f"Scenes in {START}..{END} over Thailand:", n_scenes)

def mask_clouds(img):
    return img.updateMask(img.select(QA).gte(CLEAR_THRESHOLD))

composite = filtered.map(mask_clouds).median().clip(roi)

# --- True-colour visualisation (surface reflectance x10000) ---
vis = {"bands": ["B4", "B3", "B2"], "min": 0, "max": 3000, "gamma": 1.1}
s2_map = composite.getMapId(vis)
s2_tiles = s2_map["tile_fetcher"].url_format

# --- Thin red outline of Thailand ---
outline = (ee.Image().byte()
           .paint(featureCollection=ee.FeatureCollection([ee.Feature(roi)]),
                  color=1, width=2))
out_map = outline.getMapId({"palette": ["FF3300"]})
out_tiles = out_map["tile_fetcher"].url_format

print("Got tile URLs. Building HTML...")

html = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Sentinel-2 Thailand 2026 (Median, Cloud-masked)</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  html, body { margin: 0; height: 100%; }
  #map { width: 100%; height: 100%; }
  .info-box {
    position: absolute; top: 10px; right: 10px; z-index: 1000;
    background: rgba(255,255,255,0.92); padding: 8px 12px; border-radius: 6px;
    font-family: sans-serif; font-size: 12px; max-width: 260px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.3);
  }
</style>
</head>
<body>
<div id="map"></div>
<div class="info-box">
  <b>Sentinel-2 Thailand 2026</b><br>
  Median composite (__START__ – __END__)<br>
  Cloud-masked with Cloud Score+ (&ge; __THRESH__)<br>
  True colour B4/B3/B2 &middot; GISTDA GeoAI
</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  var map = L.map('map').setView([13.0, 101.0], 6);

  var googleSat = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  }).addTo(map);
  var googleHybrid = L.tileLayer('https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  });

  var sentinel = L.tileLayer('__S2_TILES__', {
    maxZoom: 20, attribution: 'Sentinel-2 / Copernicus via Google Earth Engine', opacity: 1.0
  }).addTo(map);

  var outline = L.tileLayer('__OUT_TILES__', {
    maxZoom: 20, attribution: 'Thailand boundary (FAO GAUL)'
  }).addTo(map);

  L.control.layers(
    { "Google Satellite": googleSat, "Google Hybrid": googleHybrid },
    { "Sentinel-2 2026 (median)": sentinel, "Thailand outline": outline },
    { collapsed: false }
  ).addTo(map);
</script>
</body>
</html>
"""

html = (html
        .replace("__S2_TILES__", s2_tiles)
        .replace("__OUT_TILES__", out_tiles)
        .replace("__START__", START)
        .replace("__END__", END)
        .replace("__THRESH__", str(CLEAR_THRESHOLD)))

with io.open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("written:", OUT)
