class task:
  def __init__(self, state, description):


  	self.id = hash(description)
  	self.state = state
  	self.description = description
    
    
    
    #{“id”: 1234, “state”: “open”, “description”: “example task”}