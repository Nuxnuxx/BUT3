import mongoose, { Schema } from "mongoose";

runDb();

async function runDb() {
  try {
    await mongoose.connect("mongodb://127.0.0.1:27017/departements");
  } catch (err) {
    throw err;
  }
}

const counterSchema = new Schema({
  _id: { type: String, required: true },
  sequence_value: { type: Number, default: 0 },
});

const counterModel = mongoose.model("counter", counterSchema);

const departementsSchema = new Schema({
  nom: String,
  code: Number,
});

departementsSchema.pre("save", async function (next) {
  const doc = this;
  try {
    const counter = await counterModel.findByIdAndUpdate(
      { _id: "departementsCode" },
      { $inc: { sequence_value: 1 } },
      { new: true, upsert: true },
    );

    doc.code = counter.sequence_value;
    next();
  } catch (err) {
    return next(err);
  }
});

const Departements = mongoose.model("Departements", departementsSchema);

export default Departements;
