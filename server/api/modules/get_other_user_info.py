from flask import jsonify, request
from .execute_query import exec_query



def get_other_user_info(user_id):
    try:
        params = (user_id,)
        query = ("""SELECT 
    s.handle_name AS name,
    s.post_num AS postCount,
    s.header_image AS coverImagePath,
    s.profile_image AS profileImagePath,
    s.motto,
    s.student_intro AS introduction,
    s.web_link AS introUrl,
    COALESCE(followers.followerCount, 0) AS followerCount,
    COALESCE(following.followingCount, 0) AS followingCount,
    COALESCE(timeline.postCount, 0) AS actualPostCount
FROM 
    student_info_t s
LEFT JOIN (
    SELECT user_id_to, COUNT(*) AS followerCount
    FROM user_relation_t
    WHERE relation_code = 0
    GROUP BY user_id_to
) followers ON followers.user_id_to = s.student_id
LEFT JOIN (
    SELECT user_id_from, COUNT(*) AS followingCount
    FROM user_relation_t
    WHERE relation_code = 0
    GROUP BY user_id_from
) following ON following.user_id_from = s.student_id
LEFT JOIN (
    SELECT user_id, COUNT(*) AS postCount
    FROM timeline_t
    WHERE hidden_status = 0
    GROUP BY user_id
) timeline ON timeline.user_id = s.student_id
WHERE 
    s.student_id = %s;
                 """)
        result = exec_query(query,params)
        print(result)
        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

