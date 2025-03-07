import datetime

time_format = "%Y-%m-%d %H:%M:%S"

class Task:
    def __init__(self, id, desc, status="To do"):
        self.id = id
        self.description = desc
        self.status = status
        self.createdat = datetime.datetime.now().strftime(time_format)
        self.updatedat = None
    
    def update_description(self, new_description):
        self.description = new_description
        self.updatedat = datetime.datetime.now().strftime(time_format)
    
    def mark_in_progress(self):
        self.status = "In progress"
        self.updatedat = datetime.datetime.now().strftime(time_format)

    def mark_as_done(self):
        self.status = "Done!"
        self.updatedat = datetime.datetime.now().strftime(time_format)

    def to_dict(self):
        return {
            "description" : self.description,
            "status" : self.status,
            "created_at" : self.createdat,
            "updated_at" : self.updatedat
        }
    
