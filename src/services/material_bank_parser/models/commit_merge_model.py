from specklepy.objects import Base


class CommitMergeModel(Base):
   
    def __init__(self, material_bank_last_commit, new_commit, **kwargs):
        super().__init__(**kwargs)
        self.material_bank_last_commit = material_bank_last_commit
        self.new_commit = new_commit
