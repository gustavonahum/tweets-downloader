CREATE TABLE TWEET (
    user_name           VARCHAR2(500) NOT NULL,
    verified       varchar2(5),
    favourites_count    number(15),
    followers_count     number(15),
    friends_count       NUMBER(15),
    tweet_id            number(20),
    created_at           varchar2(20),
    lang                varchar2(2),
    retweet_count       number(15),
    favorite_count      number(15),
    is_retweet          varchar2(5),
    hashtag_count       number(3),
    text                varchar2(300),
    tweet_sentiment     varchar2(15),
    sentiment_value     float(5),
    tweet_length        number(3)
);

ALTER TABLE tweet ADD CONSTRAINT tweet_pk PRIMARY KEY ( tweet_id );