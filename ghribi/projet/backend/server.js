import express from "express";
import morgan from "morgan";
import cors from "cors";
import Departements from "./db.js";

const app = express();

app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(
  cors({
    credentials: true,
    origin: "http://localhost:5173",
  }),
);

app.get("/", async (_req, res) => {
  const result = await Departements.find();

  res.status(200).json(result);
});

app.post("/", (req, res) => {
  const { nom } = req.body;

  const departement = new Departements({
    nom,
  });

  try {
    departement.save();
  } catch (err) {
    throw err;
  }

  res.status(201).json(departement);
});

app.delete("/:id", async (req, res) => {
  const { id } = req.params;

  try {
    await Departements.findOneAndDelete({ code: id });
  } catch (err) {
    throw err;
  }

  res.status(200).json({ message: "OK" });
});

app.put("/:id", async (req, res) => {
  const { nom } = req.body;
  const { id } = req.params;

  try {
    await Departements.findOneAndUpdate({ code: id }, { nom }, { new: true });
  } catch (err) {
    throw err;
  }

  res.status(200).json({ message: "OK" });
});

app.get("/:id", async (req, res) => {
  const { id } = req.params;

  const departement = await Departements.findOne({ code: id });

  res.status(200).json(departement);
});

export default app;
