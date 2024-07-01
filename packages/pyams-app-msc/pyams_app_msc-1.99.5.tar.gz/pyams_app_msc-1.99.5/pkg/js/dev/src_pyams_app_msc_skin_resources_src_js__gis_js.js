"use strict";
(self["webpackChunkpyams_app_msc"] = self["webpackChunkpyams_app_msc"] || []).push([["src_pyams_app_msc_skin_resources_src_js__gis_js"],{

/***/ "./src/pyams_app_msc/skin/resources/src/js/_gis.js":
/*!*********************************************************!*\
  !*** ./src/pyams_app_msc/skin/resources/src/js/_gis.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./_utils */ "./src/pyams_app_msc/skin/resources/src/js/_utils.js");
/* provided dependency */ var $ = __webpack_require__(/*! jquery */ "./node_modules/jquery/dist/jquery.js");
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }

var createMap = function createMap(map, config, options, callback) {
  return new Promise(function (resolve, reject) {
    var data = map.data();
    var settings = {
      preferCanvas: data.mapLeafletPreferCanvas || false,
      attributionControl: data.mapLeafletAttributionControl === undefined ? config.attributionControl : data.mapLeafletAttributionControl,
      zoomControl: data.mapLeafletZoomControl === undefined ? config.zoomControl : data.mapLeafletZoomControl,
      crs: data.mapLeafletCrs || _utils__WEBPACK_IMPORTED_MODULE_0__["default"].getObject(config.crs) || L.CRS.EPSG3857,
      center: data.mapLeafletCenter || config.center,
      zoom: data.mapLeafletZoom || config.zoom,
      gestureHandling: data.mapLeafletWheelZoom === undefined ? !config.scrollWheelZoom : data.mapLeafletWheelZoom,
      keyboard: data.mapLeafletKeyboard === undefined ? config.keyboard && !L.Browser.mobile : data.amsLeafletKeyboard
    };
    settings = $.extend({}, settings, options);
    map.trigger('map.init', [map, settings, config]);
    var leafmap = L.map(map.attr('id'), settings),
      layersConfig = [];
    if (config.layers) {
      var _iterator = _createForOfIteratorHelper(config.layers),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var layerConfig = _step.value;
          map.trigger('map.layer.init', [map, layerConfig]);
          layersConfig.push(PyAMS_GIS.getLayer(map, leafmap, layerConfig));
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
    } else {
      layersConfig.push(L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        id: 'osm',
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }));
    }
    $.when.apply($, layersConfig).then(function () {
      for (var _len = arguments.length, layers = new Array(_len), _key = 0; _key < _len; _key++) {
        layers[_key] = arguments[_key];
      }
      for (var idx in layers) {
        layers[idx].addTo(leafmap);
      }
      if (config.zoomControl && data.mapLeafletHideZoomControl !== true) {
        L.control.scale().addTo(leafmap);
      }
      if (config.center) {
        leafmap.setView(new L.LatLng(config.center.lat, config.center.lon), config.zoom || 13);
      } else if (config.bounds) {
        leafmap.fitBounds(config.bounds);
      }
      if (config.marker) {
        var icon = L.icon({
          iconUrl: '/--static--/pyams_gis/img/marker-icon.png',
          iconSize: [25, 41],
          iconAnchor: [12, 39]
        });
        var marker = L.marker();
        marker.setIcon(icon);
        marker.setLatLng({
          lon: config.marker.lon,
          lat: config.marker.lat
        });
        marker.addTo(leafmap);
      }
      map.data('leafmap', leafmap);
      map.data('leafmap.config', config);
      map.trigger('map.finishing', [map, leafmap, config]);
      if (callback) {
        callback(leafmap, config);
      }
      map.trigger('map.finished', [map, leafmap, config]);
      resolve(leafmap);
    });
  });
};
var PyAMS_GIS = {
  /**
   * Map initialization
   *
   * @param maps: maps elements
   * @param options: optional maps configuration settings
   * @param callback: maps initialization callback
   */
  init: function init(maps, options, callback) {
    window.PyAMS_GIS = PyAMS_GIS;
    Promise.all([__webpack_require__.e(/*! import() */ "vendors-node_modules_leaflet_dist_leaflet-src_js").then(__webpack_require__.t.bind(__webpack_require__, /*! leaflet */ "./node_modules/leaflet/dist/leaflet-src.js", 23)), __webpack_require__.e(/*! import() */ "vendors-node_modules_leaflet-gesture-handling_dist_leaflet-gesture-handling_min_js").then(__webpack_require__.t.bind(__webpack_require__, /*! leaflet-gesture-handling */ "./node_modules/leaflet-gesture-handling/dist/leaflet-gesture-handling.min.js", 23)), __webpack_require__.e(/*! import() */ "vendors-node_modules_leaflet_dist_leaflet_css").then(__webpack_require__.bind(__webpack_require__, /*! ../../../../../../node_modules/leaflet/dist/leaflet.css */ "./node_modules/leaflet/dist/leaflet.css")), __webpack_require__.e(/*! import() */ "node_modules_leaflet-gesture-handling_dist_leaflet-gesture-handling_css").then(__webpack_require__.bind(__webpack_require__, /*! ../../../../../../node_modules/leaflet-gesture-handling/dist/leaflet-gesture-handling.css */ "./node_modules/leaflet-gesture-handling/dist/leaflet-gesture-handling.css"))]).then(function () {
      var $maps = $.map(maps, function (elt) {
        return new Promise(function (resolve, reject) {
          var map = $(elt),
            data = map.data(),
            config = data.mapConfiguration;
          if (config) {
            resolve(createMap(map, config, options, callback));
          } else {
            $.get(data.mapConfigurationUrl || 'get-map-configuration.json', function (config) {
              resolve(createMap(map, config, options, callback));
            });
          }
        });
      });
      $.when.apply($, $maps).then();
    });
  },
  /**
   * Get layer definition
   *
   * @param map: source map element
   * @param leafmap: current Leaflet map
   * @param layer: current layer definition
   */
  getLayer: function getLayer(map, leafmap, layer) {
    var factory = _utils__WEBPACK_IMPORTED_MODULE_0__["default"].getObject(layer.factory);
    if (factory !== undefined) {
      delete layer.factory;
      var deferred = [];
      if (layer.dependsOn) {
        for (var name in layer.dependsOn) {
          if (!layer.dependsOn.hasOwnProperty(name)) {
            continue;
          }
          if (_utils__WEBPACK_IMPORTED_MODULE_0__["default"].getObject(name) === undefined) {
            deferred.push(_utils__WEBPACK_IMPORTED_MODULE_0__["default"].getScript(layer.dependsOn[name]));
          }
        }
        delete layer.dependsOn;
      }
      if (deferred.length > 0) {
        $.when.apply($, deferred);
      }
      return factory(map, leafmap, layer);
    }
  },
  /**
   * Layers factories
   */
  factory: {
    GeoJSON: function GeoJSON(map, leafmap, layer) {
      var url = layer.url;
      delete layer.url;
      var result = L.geoJSON(null, layer);
      map.on('map.finished', function (evt, map, leafmap, config) {
        $.get(url, function (data) {
          result.addData(data.geometry, {
            style: layer.style
          });
          if (config.fitLayer === layer.name) {
            leafmap.fitBounds(result.getBounds());
          }
        });
      });
      return result;
    },
    TileLayer: function TileLayer(map, leafmap, layer) {
      var url = layer.url;
      delete layer.url;
      return L.tileLayer(url, layer);
    },
    WMS: function WMS(map, leafmap, layer) {
      var url = layer.url;
      delete layer.url;
      return L.tileLayer.wms(url, layer);
    },
    Geoportal: {
      WMS: function WMS(map, leafmap, layer) {
        _utils__WEBPACK_IMPORTED_MODULE_0__["default"].getCSS('/--static--/pyams_gis/css/leaflet-gp-3.0.2.min.css', 'geoportal');
        return L.geoportalLayer.WMS(layer);
      }
    },
    ESRI: {
      Feature: function Feature(map, leafmap, layer) {
        return L.esri.featureLayer(layer);
      }
    },
    Google: function Google(map, leafmap, layer) {
      var apiKey = layer.apiKey;
      delete layer.apiKey;
      if (_utils__WEBPACK_IMPORTED_MODULE_0__["default"].getObject('window.google.maps') === undefined) {
        var script = _utils__WEBPACK_IMPORTED_MODULE_0__["default"].getScript('https://maps.googleapis.com/maps/api/js?key=' + apiKey);
        $.when.apply($, [script]);
      }
      return L.gridLayer.googleMutant(layer);
    }
  }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (PyAMS_GIS);

/***/ })

}]);
//# sourceMappingURL=src_pyams_app_msc_skin_resources_src_js__gis_js.js.map