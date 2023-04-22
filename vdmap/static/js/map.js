$(window).on("load", () => {
    const Map = ol.Map;
    const Overlay = ol.Overlay;
    const View = ol.View;
    const TileLayer = ol.layer.Tile;
    const OSM = ol.source.OSM;
    const Point = ol.geom.Point;
    const Select = ol.interaction.Select;
    const Feature = ol.Feature;
    const SourceVector = ol.source.Vector;
    const LayerVector = ol.layer.Vector
    const Fill = ol.style.Fill;
    const Stroke = ol.style.Stroke;
    const Style = ol.style.Style
    const Circle = ol.style.Circle
    let map = null;
    let route = null;
    let routeVector = null;
    let routeLayer = null;
    ol.proj.useGeographic();
    $.get({
        url: "/map/get_points"
    }).done((r) => {
        map = new Map({
            layers: [
                new TileLayer({source: new OSM()}),
            ],
            view: new View({
                center: r.center.coordinates,
                zoom: 17,
            }),
            target: 'map',
        });
        const marker_fill = new Fill({
            color: 'rgba(255,255,255,0.4)',
        });
        const marker_stroke = new Stroke({
            color: '#3399CC',
            width: 1.25,
        });
        const route_fill = new Fill({
            color: '#ff0000',
        });
        const route_stroke = new Stroke({
            color: '#ff0000',
            width: 1.25,
        });

        var markersLayer = new LayerVector({
            source: new SourceVector(),
            style: new Style({
                image: new Circle({
                    fill: marker_fill,
                    stroke: marker_stroke,
                    radius: 10,
                }),
                fill: marker_fill,
                stroke: marker_stroke,
            })
        });
        map.addLayer(markersLayer);
        r.pavilions.forEach((e) => {
            let f = new Feature(new Point(e.coordinates));
            f.attributes = {"name": e.name, "description": e.description}
            markersLayer.getSource().addFeature(f);
        })
        var select = new Select({
            condition: ol.events.condition.click,
        });
        map.addInteraction(select);
        select.on('select', (e) => {
        });
        routeVector = new SourceVector({});
        routeLayer = new LayerVector({
            source: routeVector,
            style: new Style({
                fill: route_fill,
                stroke: route_stroke
            })
        });
        map.addLayer(routeLayer);
    });
    $(".option").click((e) => {
        $(".options-container").addClass("moved-left");
        $(`.routes-block[data-id="${$(e.currentTarget).data("target")}"]`).addClass("moved-center");
        $(".routes-div").css("overflow-y", "auto");

    });
    $(".back").click((e) => {
        $(".routes-block").removeClass("moved-center");
        $(".options-container").removeClass("moved-left");
        $(".routes-div").css("overflow-y", "hidden");
    });
    $(".magnifer-container > div").click((e) => {
        $(e.currentTarget).parent().parent().parent().find(".description-collapse").toggleClass("collapse-active")
    });
    $(".magnifer").click((e) => {
        let q = $(e.currentTarget).parent().parent().parent();
        map.getView().setCenter([q.data("coord-x"), q.data("coord-y")])
    });
    $(".build-route").click((e) => {
        let s1 = $(".select-start").find(":selected")
        let p1 = [parseFloat(s1.data("coord-x")), parseFloat(s1.data("coord-y"))]
        let s2 = $(".select-end").find(":selected")
        let p2 = [parseFloat(s2.data("coord-x")), parseFloat(s2.data("coord-y"))]
        $.get({
            url: "/map/build_route",
            data: {
                "p1": p1, "p2": p2
            }
        }).done((r) => {
            if (r.ok) {
                if (route) {
                    routeLayer.getSource().removeFeature(route)
                }
                const featureLine = new Feature({
                    geometry: new ol.geom.LineString([p1].concat(r.route))
                });
                map.getView().setCenter(p1)
                route = featureLine
                routeVector.addFeature(featureLine);
                $(".time-placeholder").text(r.time)
            }
        });
    })
    $("#save-route").click(() => {
        let s1 = $(".select-start").find(":selected")
        let p1 = [parseFloat(s1.data("coord-x")), parseFloat(s1.data("coord-y"))]
        let s2 = $(".select-end").find(":selected")
        let p2 = [parseFloat(s2.data("coord-x")), parseFloat(s2.data("coord-y"))]
        $.post({
            url: "/map/save_route",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                n1: s1.text(),
                p1: p1,
                n2: s2.text(),
                p2: p2
            })
        }).done((r) => {
            if (r.ok) {
                alert("Маршрут сохранён")
            }
        })
    });
    $(".saved-route").click((e) => {
        let t = $(e.currentTarget);
        $.get({
            url: "/map/build_route",
            data: {
                "p1": t.data("p1"), "p2": t.data("p2")
            }
        }).done((r) => {
            if (r.ok) {
                if (route) {
                    routeLayer.getSource().removeFeature(route)
                }
                const featureLine = new Feature({
                    geometry: new ol.geom.LineString([t.data("p1")].concat(r.route))
                });
                map.getView().setCenter(t.data("p1"))
                route = featureLine
                routeVector.addFeature(featureLine);
            }
        });
    })
});