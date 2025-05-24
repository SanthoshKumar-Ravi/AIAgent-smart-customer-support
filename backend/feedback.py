def store_feedback(redis, feedback):
    redis.hset(feedback.query_id, mapping={
        "rating": feedback.rating,
        "comment": feedback.comment
    })
