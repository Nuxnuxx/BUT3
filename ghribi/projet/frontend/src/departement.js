import { redirect } from "react-router-dom";
import {
  createDepartement,
  deleteDepartement,
  getDepartement,
  getDepartementById,
  updateDepartement,
} from "./fetchDepartement";

export async function loader() {
  const departements = await getDepartement();
  return { departements };
}

export async function action({ request }) {
  const formData = await request.formData();
  let departement;
  if (formData.get("feat") == "create") {
    departement = await createDepartement(formData.get("nom"));
  }
  if (formData.get("feat") == "delete") {
    departement = await deleteDepartement(formData.get("code"));
  }
	console.log(departement)
  return { departement };
}

export async function updateAction({ request, params }) {
  const formData = await request.formData();
  await updateDepartement(formData.get("nom"), params.id);
  return redirect("/departements");
}

export async function updateLoader({ params }) {
  const departement = await getDepartementById(params.id);
  return { departement };
}
