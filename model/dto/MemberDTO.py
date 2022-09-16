class MemberDTO:
    def __init__(self,newMemberId, newMemberName, newAge, newPhone, newGender, newClubName, newRating, newEnroll):
        self.memberId = newMemberId
        self.memberName = newMemberName
        self.age = newAge 
        self.phone = newPhone
        self.gender = newGender
        self.clubName = newClubName
        self.rating = newRating
        self.enroll = newEnroll
        
    def getMemberId(self):
        return self.memberId
    
    def setMemberId(self, newMemberId):
        self.memberId = newMemberId
        
    def getMemberName(self):
        return self.memberName
    
    def setMemberName(self, newMemberName):
        self.memberName = newMemberName
        
    def getAge(self):
        return self.age
    
    def setAge(self, newAge):
        self.age = newAge
        
    def getPhone(self):
        return self.phone
    
    def setPhone(self, newPhone):
        self.phone = newPhone
        
    def getGender(self):
        return self.gender
    
    def setGender(self, newGender):
        self.gender = newGender
        
    def getClubName(self):
        return self.clubName
    
    def setClubName(self, newClubName):
        self.clubName = newClubName
        
    def getRating(self):
        return self.rating
    
    def setRating(self, newRating):
        self.rank = newRating
    
    def getEnroll(self):
        return self.enroll
    
    def setEnroll(self, newEnroll):
        self.enroll = newEnroll
        
    def __str__(self):
        return '아이디 : ' + str(self.memberId) + ', 회원명 : ' + self.memberName + ', 나이 : ' + str(self.age) + ', 전화번호 : ' + self.phone + ', 성별 : ' + str(self.gender) + ', 클럽명 : ' + self.clubName + ', 랭크 : ' + self.rating + ', 등록일자 : ' + str(self.enroll)


# test용 코드
if __name__ == '__main__':
    member = MemberDTO(15, '종국', 42, "010-1234-5678", 'm', "짐종국", "SS", '1999-05-01')
    print(member)           
        