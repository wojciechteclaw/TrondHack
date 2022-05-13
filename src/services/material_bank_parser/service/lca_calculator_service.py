class LCACalculatorService:
    
    lca_factor = 4.15

    @staticmethod
    def parameters_enrichement(element):
        volume = element.volume / (1000**3)
        mass = volume * 7850
        element["LCA"] = {"A1-A3":{
                                    "value": mass * LCACalculatorService.lca_factor,
                                    "unit": "kgCO2eq"
                                  }}
        element["mass"] = {"value": mass,
                           "unit": "kg"
                          }
        return element
