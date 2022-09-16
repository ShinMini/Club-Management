class ClubDTO:
   # 생성자 생성과 동시에 지역변수 선언함. (self)활용해 호출 및 선언
   def __init__(self, newClubId, newClubName):
      self.clubId = newClubId
      self.clubName= newClubName
      
   # getter & setter
   def getClubId(self):
      return self.clubId
   
   def setClubId(self, newClubId):
      self.clubId = newClubId

   def getClubName(self):
      return self.clubName
   
   def setClubName(self, newClubName):
      self.clubName = newClubName
   
   def __str__(self):
      return '클럽 아이디: ' + str(self.clubId) + ', 클럽명: ' + self.clubName