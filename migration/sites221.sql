BEGIN;

-- blog related stuff

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
    "tags" varchar(255) NOT NULL,
    "template_name" varchar(200)
);

INSERT INTO "blog_entry"
    SELECT id, title, datetime, content, sticky, published, comments_enabled, slug, tags, null
    FROM "blog_entry_old";

DROP TABLE "blog_entry_old";

-- created for the first time
CREATE TABLE "sites_per_entry" (
    "id" integer NOT NULL PRIMARY KEY,
    "entry_id" integer NOT NULL,
    "site_id" integer NOT NULL,
    UNIQUE ("entry_id", "site_id")
);

-- insert default values into new table
INSERT INTO "sites_per_entry" (entry_id, site_id)
    SELECT id, 1
    FROM "blog_entry";


-- flatpage related stuff

-- created for the first time
CREATE TABLE "sites_per_flatpage" (
    "id" integer NOT NULL PRIMARY KEY,
    "flatpage_id" integer NOT NULL,
    "site_id" integer NOT NULL,
    UNIQUE ("flatpage_id", "site_id")
);

-- forgot to delete this at production
DROP TABLE "flatpages_flatpage_old";

ALTER TABLE "flatpages_flatpage" RENAME TO "flatpages_flatpage_old";

CREATE TABLE "flatpages_flatpage" (
    "id" integer NOT NULL PRIMARY KEY,
    "url" varchar(100) NOT NULL,
    "title" varchar(200) NOT NULL,
    "content" text NOT NULL,
    "enable_comments" bool NOT NULL,
    "registration_required" bool NOT NULL,
    "template_name" varchar(200),
    "show_on_homepage" bool NOT NULL,
    "tags" varchar(255)
);

INSERT INTO "flatpages_flatpage"
    SELECT id, url, title, content, enable_comments, registration_required, template_name, show_on_homepage, tags
    FROM "flatpages_flatpage_old";

DROP TABLE "flatpages_flatpage_old";

-- migrate flatpage sites to new db schema
INSERT INTO "sites_per_flatpage" (flatpage_id, site_id)
    SELECT flatpage_id, site_id
    FROM "flatpages_flatpage_sites";

DROP TABLE "flatpages_flatpage_sites";

COMMIT;