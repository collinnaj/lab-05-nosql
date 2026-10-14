db = db.getSiblingDB("bookstore");
db.authors.drop();

let authors = JSON.parse(
    fs.readFileSync("authors.json", "utf8")
);

db.authors.insertMany(authors);
db.books.drop();
let books = JSON.parse(fs.readFileSync("books.json", "utf8"));
db.books.insertMany(books);
db.authors.find();
db.books.find();

db.books.insertMany([
    {
        title: "The Mountain Path",
        published_year: 2022,
        author_ids: ["author_004"]
    },
    {
        title: "Austen's Garden",
        published_year: 2024,
        author_ids: ["author_001", "author_004"]
    }
]);

db.authors.insertOne({
    _id: "author_004",
    name: "Alex Rivera",
    nationality: "American",
    bio: {
        short: "A fictional novelist",
        long: "Alex Rivera is a fictional author created for this MongoDB lab."
    }
});

db.books.find({
    author_ids: {
        $in: ["author_001", "author_004"]
    }
});
