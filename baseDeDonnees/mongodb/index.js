import { MongoClient } from "mongodb";

const url = "mongodb://localhost:27017";
const client = new MongoClient(url);

const dbName = "test";

async function main() {
  await client.connect();
  console.log("Connected successfully to server");
  const db = client.db(dbName);

  await db.createCollection("people");

  const collection = db.collection("people");

  // const users = [
  //   {
  //     name: "John Doe",
  //     age: 30,
  //     sexe: "f",
  //   },
  //   {
  //     name: "Alice Smith",
  //     age: 25,
  //     sexe: "m",
  //   },
  //   {
  //     name: "Bob Johnson",
  //     age: 35,
  //     sexe: "m",
  //   },
  // ];
  //
  // await collection.insertMany(users);

  // const collectionPrint = await collection.find({}).toArray();
  // console.log(collectionPrint)
  //
  // const collectionPrintWithFilter = await collection.find({sexe: "m"}).toArray();
  // console.log(collectionPrintWithFilter)

  // make the first document with sexe = m
  const collectionFirstModified = await collection.findOneAndUpdate(
    { sexe: "m" },
    { $set: { sexe: "f" } },
  );
  console.log(collectionFirstModified);

  // update all record name to sausage
  const collectionAllModified = await collection.updateMany(
    {},
    { $set: { name: "sausage" } },
  );
}

main()
  .then(console.log)
  .catch(console.error)
  .finally(() => client.close());
