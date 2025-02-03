CREATE TABLE genres (
  genre_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

INSERT INTO genres (name) VALUES 
('Fantasy'),
('Science Fiction'),
('Mystery'),
('Thriller');

CREATE TABLE novels (
  novel_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  description TEXT,
  published_date TEXT
);

INSERT INTO novels (title, author, description, published_date) VALUES
('The Cosmic Odyssey', 'Jane Doe', 'An epic space adventure', '2025-01-15'),
('Shadows in the Mist', 'John Smith', 'A chilling mystery set in a small town', '2025-02-01');

CREATE TABLE chapters (
  chapter_id INTEGER PRIMARY KEY,
  novel_id INTEGER,
  chapter_number INTEGER,
  title TEXT,
  content TEXT,
  FOREIGN KEY (novel_id) REFERENCES novels(novel_id)
);

INSERT INTO chapters (novel_id, chapter_number, title, content) VALUES
(1, 1, 'Launch Day', 'The spacecraft hummed to life as Captain Sarah...'),
(1, 2, 'Strange Signals', 'Deep in the void of space, an unexpected transmission...'),
(2, 1, 'Return to Foggy Creek', 'Detective Mike Harper stepped out of his car...');
