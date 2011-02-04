BEGIN;

ALTER TABLE "users_userprofile" RENAME TO "users_userprofile_old";

CREATE TABLE "subscribed_entries_per_profile" (
    "id" integer NOT NULL PRIMARY KEY,
    "userprofile_id" integer NOT NULL,
    "entry_id" integer NOT NULL,
    UNIQUE ("userprofile_id", "entry_id")
);

CREATE TABLE "users_userprofile" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE,
    "avatar" varchar(200) NOT NULL,
    "web_site" varchar(200) NOT NULL,
    "comments_count" integer unsigned NOT NULL,
    "last_modified" datetime NOT NULL
);

INSERT INTO "users_userprofile"
    SELECT id, user_id, avatar, web_site, 0, last_modified
        FROM "users_userprofile_old";

DROP TABLE "users_userprofile_old";

-- dropping language field from blogs
ALTER TABLE "blog_entry" RENAME TO "blog_entry_old";

CREATE TABLE "blog_entry" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(80) NOT NULL,
    "datetime" datetime NOT NULL,
    "content" text NOT NULL,
    "sticky" bool NOT NULL,
    "published" bool NOT NULL,
    "comments_enabled" bool NOT NULL,
    "slug" varchar(100) NOT NULL,
    "tags" varchar(255) NOT NULL
);

INSERT INTO "blog_entry"
    SELECT id, title, datetime, content, sticky, published, comments_enabled, slug, tags
        FROM "blog_entry_old";

DROP TABLE "blog_entry_old";

-- dropping language field from flatpages
ALTER TABLE "flatpages_flatpage" RENAME TO "flatpages_flatpage_old";

CREATE TABLE "flatpages_flatpage" (
    "id" integer NOT NULL PRIMARY KEY,
    "url" varchar(100) NOT NULL,
    "title" varchar(200) NOT NULL,
    "content" text NOT NULL,
    "enable_comments" bool NOT NULL,
    "template_name" varchar(70) NOT NULL,
    "registration_required" bool NOT NULL,
    "show_on_homepage" bool NOT NULL,
    "tags" varchar(255)
);

INSERT INTO "flatpages_flatpage"
    SELECT id, url, title, content, enable_comments, template_name, registration_required, show_on_homepage, ""
        FROM "flatpages_flatpage_old";

COMMIT;