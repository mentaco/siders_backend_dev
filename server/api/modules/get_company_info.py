from flask import jsonify, request
from .execute_query import exec_query

def get_company_info(user_id):
    try:
        params = (user_id,)
        query = ("""SELECT 
    c.company_name AS company_name,
    c.company_header_image AS company_header_image,
    c.company_logomark AS company_logomark,
    c.company_explanation AS company_explanation,
    c.company_web AS company_web,
    c.company_mail_address AS company_mail_address,
    c.tel_num AS tel_num,
    c.company_address AS company_address,
    c.postalcode AS postalcode,
    COALESCE(followers.followerCount, 0) AS followerCount,
    COALESCE(following.followingCount, 0) AS followingCount,
    COALESCE(timeline.postCount, 0) AS actualPostCount
FROM 
    company_info_t c
LEFT JOIN (
    SELECT user_id_to, COUNT(*) AS followerCount
    FROM user_relation_t
    WHERE relation_code = 0
    GROUP BY user_id_to
) followers ON followers.user_id_to = c.company_id
LEFT JOIN (
    SELECT user_id_from, COUNT(*) AS followingCount
    FROM user_relation_t
    WHERE relation_code = 0
    GROUP BY user_id_from
) following ON following.user_id_from = c.company_id
LEFT JOIN (
    SELECT user_id, COUNT(*) AS postCount
    FROM timeline_t
    WHERE hidden_status = 0
    GROUP BY user_id
) timeline ON timeline.user_id = c.company_id
WHERE 
    c.company_id = %s;
                 """)
        result = exec_query(query,params)
        print(result)
        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

