import io

SRC = r"E:\Gistda_GeoAI_VibeCode\GISTDA GeoAI & Vibe Coding - Material-20260713T022955Z-2-001\GISTDA GeoAI & Vibe Coding - Material\GEE4NRE 20240131-0202\Example\Thailand.geojson"
DST = r"E:\Gistda_GeoAI_VibeCode\GISTDA GeoAI & Vibe Coding - Material-20260713T022955Z-2-001\GISTDA GeoAI & Vibe Coding - Material\GEE4NRE 20240131-0202\Example\Thailand.html"

with io.open(SRC, "r", encoding="utf-8") as f:
    geojson_text = f.read()

html = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Thailand GeoJSON - Interactive Map</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  html, body { margin: 0; height: 100%; }
  #map { width: 100%; height: 100%; }
  .info-box {
    position: absolute; top: 10px; right: 10px; z-index: 1000;
    background: rgba(255,255,255,0.9); padding: 8px 12px; border-radius: 6px;
    font-family: sans-serif; font-size: 13px; box-shadow: 0 1px 4px rgba(0,0,0,0.3);
  }
</style>
</head>
<body>
<div id="map"></div>
<div class="info-box">Thailand boundary (EPSG:4326) — GISTDA GEE4NRE</div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  var thailandData = __GEOJSON__;

  var map = L.map('map', { zoomControl: true });

  var googleRoadmap = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  });
  var googleSatellite = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  });
  var googleHybrid = L.tileLayer('https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  });
  var googleTerrain = L.tileLayer('https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', {
    maxZoom: 20, subdomains: ['mt0','mt1','mt2','mt3'], attribution: '&copy; Google Maps'
  });

  googleRoadmap.addTo(map);

  var geoLayer = L.geoJSON(thailandData, {
    style: {
      color: '#ff3300',
      weight: 2,
      fillColor: '#ff9900',
      fillOpacity: 0.15
    },
    onEachFeature: function (feature, layer) {
      var props = feature.properties || {};
      var rows = Object.keys(props).map(function(k){ return '<b>' + k + ':</b> ' + props[k]; }).join('<br>');
      if (rows) layer.bindPopup(rows);
    }
  }).addTo(map);

  map.fitBounds(geoLayer.getBounds());

  L.control.layers({
    "Google Roadmap": googleRoadmap,
    "Google Satellite": googleSatellite,
    "Google Hybrid": googleHybrid,
    "Google Terrain": googleTerrain
  }, {
    "Thailand boundary": geoLayer
  }, { collapsed: false }).addTo(map);
</script>
</body>
</html>
"""

html = html.replace("__GEOJSON__", geojson_text)

with io.open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print("written:", DST)
