# from model.dto.ClubDTO import ClubDTO
from model.dto.MemberDTO import MemberDTO
from dbutil import getConnect

# 직원 등록


class MemberDAO:
    # CREATE MEMBER
    def insert_member(self, m):
        try:
            conn = getConnect()
            cur = conn.cursor()

            sql_query = 'insert into member(member_id, member_name, age, phone, gender, club_name, rating, enroll) values ({0}, "{1}", {2}, "{3}", "{4}", "{5}", "{6}", "{7}")'.format(
                m.getMemberId(), m.getMemberName(), m.getAge(), m.getPhone(), m.getGender(), str(m.getClubName()), m.getRating(), m.getEnroll())
            print(sql_query)

            cur.execute(sql_query)
            conn.commit()
            print("---------------- 성공 -------------------")
        except Exception as e:
            print("---------------- 실패 -------------------")
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    # READ ALL MEMBERS

    def search_all_members(self):

        result = []
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('select * from member')
            conn.commit()
            rows = cur.fetchall()

            for r in rows:
                temp = '{"member_id":%s, "member_name": "%s", "age": %s, "phone": "%s", "gender": "%s", "club_name": "%s", "rating": "%s", "enroll": "%s"}' % (
                    r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
                result.append(temp)

            return result

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()

# SEARCH A MEMBER WHERE MEMBER ID
    def search_member(self, m):
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute(('select * from member where member_id = %s'), m)
            conn.commit()
            result = cur.fetchone()

            return result

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()

# UPDATE A MEMBER WHERE MEMBER ID
    def update_member(self, memberid, newName):
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute(('update member set member_name = %s where member_id = %s'),
                        (newName, memberid))
            cur.execute(
                ('select * from member where member_id = %s'), memberid)
            print(cur.fetchone())
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()


# DELETE A MEMBER WHERE MEMBER ID


    def delete_members(self, m):
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute(('delete from member where member_id = %s'), m)
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()
