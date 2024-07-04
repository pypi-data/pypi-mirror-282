class Result:
  def __init__(
      self, 
      row_count:int = None,
      last_id:int = None,
      data:list = None
      ):
    self.row_count=row_count
    self.last_id=last_id
    self.data = data