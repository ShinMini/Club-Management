from unittest import result
from model.dto.ClubDTO import ClubDTO
from dbutil import getConnect

# 클럽 등록
class ClubDAO:
   # CREATE club
   def insert_club(self, c):
      try:
         conn = getConnect()
         cur = conn.cursor()

         sql_query = 'insert into club(club_id, club_name) values ({0}, "{1}")'.format(
               c.getClubId(), c.getClubName())

         cur.execute(sql_query)
         conn.commit()

      except Exception as e:
         print(e)
         conn.rollback()
      finally:
         cur.close()
         conn.close()

   # READ ALL CLUBS
   def search_all_clubs(self):
      result = []

      try:
         conn = getConnect()
         cur = conn.cursor()
         cur.execute('select * from club')
         conn.commit()

         rows = cur.fetchall()

         for r in rows:
            temp = '{"club_id":%s, "club_name":"%s"}' % (r[0], r[1])
            result.append(temp)

         return result

      except Exception as e:
         conn.rollback()

      finally:
         cur.close()
         conn.close()


    # READ A CLUB WHERE CLUB ID
   def search_club(self, c):
      try:
         conn = getConnect()
         cur = conn.cursor()

         cur.execute(('select * from club where club_id= %s'), c)
         conn.commit()

         result = cur.fetchone()

         return result

      except Exception as e:
         conn.rollback()
      finally:
         cur.close()
         conn.close()

   # UPDATE A CLUB WHERE CLUB ID
   def update_club(self, clubid, newClubName):
      try:
         conn = getConnect()
         cur = conn.cursor()
         cur.execute(('update club set club_name = %s where club_id= %s'),
                  (newClubName, clubid))
         cur.execute(
               ('select * from club where club_name= %s'), newClubName)
         print(cur.fetchone())

         conn.commit()
      except Exception as e:
         print(e)
         conn.rollback()
      finally:
         cur.close()
         conn.close()


# DELETE A CLUB WHERE CLUB ID
   def delete_club(self, c):
      try:
         conn = getConnect()
         cur = conn.cursor()
         cur.execute(('delete from club where club_id= %s'), c)
         conn.commit()
      except Exception as e:
         conn.rollback()
      finally:
         cur.close()
         conn.close()