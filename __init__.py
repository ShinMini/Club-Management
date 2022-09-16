from flask import Flask, request, render_template, jsonify
from model.dto.MemberDTO import MemberDTO
from model.dao.MemberDAO import MemberDAO
from model.dto.ClubDTO import ClubDTO
from model.dao.ClubDAO import ClubDAO

app = Flask(__name__)


@app.route("/")
def intro():
    print("=======intro()=======")
    return render_template("index.html")

# Member url ----------------------------------------------------#


@app.route('/member')
def page():
    return render_template("page/memberView.html")

# sub member url ------------------------------------------------#


@app.route('/member/insert')
def mem_insert():
    return render_template("page/member/insert.html")


@app.route('/member/search')
def mem_search():
    return render_template("page/member/search.html")


@app.route('/member/update')
def mem_update():
    return render_template("page/member/update.html")


@app.route('/member/delete')
def mem_delete():
    return render_template("page/member/delete.html")

#----------------------------------------------------------------#

# CREATE(INSERT)


@app.route('/member/insert/enroll', methods=['POST', 'GET'])
def member_insert():
    memid = request.form.get("memid")
    memname = request.form.get("memname")
    age = request.form.get("age")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    clubname = request.form.get("clubName")
    rating = request.form.get("rating")
    enroll = request.form.get("enroll")

    member = MemberDTO(memid, memname, age, phone,
                       gender, clubname, rating, enroll)
    memberDao = MemberDAO()
    memberDao.insert_member(member)

    return render_template("page/member/insert.html")

# READ(SEARCH)


@app.route('/member/search/one', methods=['POST', 'GET'])
def member_search():
    memid = request.form.get("memid")
    memname = request.form.get("memname")
    age = request.form.get("age")
    memberDao = MemberDAO()
    result = memberDao.search_member(memid)

    if result is None:
        return "해당 조회 결과가 없습니다."

    members = '{"member_id":%s, "member_name": "%s", "age": %s, "phone": "%s", "gender": "%s", "club_name": "%s", "rating": "%s", "enroll": "%s"}' % (
        result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
    return members


@app.route('/member/search/all', methods=['POST', 'GET'])
def member_searchAll():
    memberDao = MemberDAO()
    result = memberDao.search_all_members()

    return jsonify(result)


# UPDATE
@ app.route('/member/update/enroll', methods=['get', 'post'])
def member_update():
    memid = request.form.get("memid")
    memname = request.form.get("memname")
    memberDao = MemberDAO()
    memberDao.update_member(memid, memname)
    return render_template("page/member/update.html")

# DELETE


@ app.route('/member/delete/enroll', methods=['POST', 'GET'])
def member_delete():
    memid = request.form.get("memid")
    memberDao = MemberDAO()
    memberDao.delete_members(memid)
    return render_template("page/member/delete.html")


# Club url ------------------------------------------------------#

@app.route('/club')
def club_page():
    return render_template("page/clubView.html")

# sub member url ------------------------------------------------#


@app.route('/club/insert')
def c_insert():
    return render_template("page/club/insert.html")


@app.route('/club/search')
def c_search():
    return render_template("page/club/search.html")


@app.route('/club/update')
def c_update():
    return render_template("page/club/update.html")


@app.route('/club/delete')
def c_delete():
    return render_template("page/club/delete.html")

#----------------------------------------------------------------#

# CREATE(INSERT)


@app.route('/club/insert/enroll', methods=['POST', 'GET'])
def club_insert():
    clubid = request.form.get("clubid")
    clubname = request.form.get("clubname")

    club = ClubDTO(clubid, clubname)
    clubDao = ClubDAO()
    clubDao.insert_club(club)

    return render_template("page/club/insert.html")

# READ(SEARCH)


@app.route('/club/search/one', methods=['POST', 'GET'])
def club_search():
    print("================init==============")
    clubid = request.form.get("clubid")
    clubname = request.form.get("clubname")
    clubDao = ClubDAO()
    result = clubDao.search_club(clubid)

    if result is None:
        return "해당 조회 결과가 없습니다."

    club = '{"club_id":%s, "club_name":"%s"}' % (result[0], result[1])

    return club

# READ ALL(SEARCH)

@app.route('/club/search/all', methods=['POST', 'GET'])
def club_searchAll():
    clubDao = ClubDAO()

    result = clubDao.search_all_clubs()

    return jsonify(result)

# CHECK
@app.route('/club/search/check', methods=['POST', 'GET'])
def club_check():
    clubid = request.form.get("clubid")

    print(clubid)
    clubDao = ClubDAO()
    result = clubDao.search_club(clubid)
    print(result)

    if result is None:
        return "해당 아이디 조회 결과가 없습니다."

    clubs = '{클럽 아이디: %s, 클럽 이름: "%s"}' % ( result[0], result[1])

    return clubs

# UPDATE
@app.route('/club/update/enroll', methods=['get', 'post'])
def club_update():
    clubid = request.form.get("clubid")
    clubname = request.form.get("clubname")

    clubDao = ClubDAO()
    clubDao.update_club(clubid, clubname)

    return render_template("page/club/update.html")

# DELETE


@app.route('/club/delete/enroll', methods=['POST', 'GET'])
def club_delete():
    clubid= request.form.get("clubid")

    clubDao = ClubDAO()
    clubDao.delete_club(clubid)
    return render_template("page/club/delete.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
