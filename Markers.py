import Adams

for model in Adams.Models.values():
    for part in model.Parts.values():
        for marker in part.Markers.values():
            marker.hide()