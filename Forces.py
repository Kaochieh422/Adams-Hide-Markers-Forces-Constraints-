import Adams
        
for model in Adams.Models.values():
    for constraint in model.Forces.values():
        constraint.hide()