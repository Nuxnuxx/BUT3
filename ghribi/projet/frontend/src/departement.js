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
  const departement = await createDepartement(formData.get("nom"));
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

export async function deleteAction({ request }) {
  const formData = await request.formData();
  const departement = await deleteDepartement(formData.get("nom"));
  return { departement };
}
