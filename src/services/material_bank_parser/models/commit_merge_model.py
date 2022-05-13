from specklepy.objects import Base

class CommitMergeModel():
   
    def __init__(self, material_bank_last_commit, new_commit, **kwargs):
        super().__init__(**kwargs)
        self.material_bank_last_commit = material_bank_last_commit
        self.new_commit = new_commit

    def merge(self):
        objects = list()
        if self.material_bank_last_commit:
            objects = self.material_bank_last_commit['@data'][0][0]
        for new_item in self.new_commit['@data'][0][0]:
            objects.append(new_item)
        my_final_object = Base()
        my_final_object['@data'] = [[objects]]
        print(my_final_object)
        return my_final_object
