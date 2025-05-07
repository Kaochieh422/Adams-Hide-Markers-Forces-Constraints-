# @TSENG KAO CHIEH
import Adams
   
for model in Adams.Models.values():
    for constraint in model.Constraints.values():
        constraint.hide()
        
for model in Adams.Models.values():
    for constraint in model.Forces.values():
        constraint.hide()
