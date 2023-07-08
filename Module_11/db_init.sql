-- Create users table
CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY (user_id)
);

-- Insert data into users table
INSERT INTO users (first_name, last_name) VALUES
    ('Johnny', 'Boy'),
    ('Jackson', 'Smith'),
    ('Amanda', 'Farmer');

-- Create books table
CREATE TABLE books (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY (book_id)
);

-- Create store table
CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY (store_id)
);

-- Insert data into books table
INSERT INTO books (book_name, details, author) VALUES
    ('The Lord of the Rings', 'Epic fantasy trilogy in Middle-earth', 'J.R.R. Tolkien'),
    ('To Kill a Mockingbird', 'Classic novel about racial injustice', 'Harper Lee'),
    ('The Great Gatsby', 'Roaring 1920s and pursuit of the American Dream', 'F. Scott Fitzgerald'),
    ('The Girl with the Dragon Tattoo', 'Compelling crime thriller with complex characters', 'Stieg Larsson'),
    ('The Hobbit', 'Adventure in Middle-earth with Bilbo Baggins', 'J.R.R. Tolkien'),
    ('The Maze Runner', 'Thrilling dystopian adventure in a mysterious maze', 'James Dashner'),
    ('The Giver', 'Dystopian tale of a controlled society and a young boys awakening', 'Lois Lowry'),
    ('Catch-22', 'Satirical war novel exposing the absurdities of bureaucracy', 'Joseph Heller'),
    ('The Outsiders', 'Coming-of-age story about rival teenage gangs in 1960s Oklahoma', 'S.E. Hinton');

-- Create wishlist table
CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Insert data into wishlist table
INSERT INTO wishlist (user_id, book_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3);

-- Insert data into store table
INSERT INTO store (locale) VALUES
    ('901 South Ave, Dallas, TX 75201');
