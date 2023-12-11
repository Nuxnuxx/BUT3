export const getDepartementById = async (id) => {
  try {
    const result = await fetch(`${import.meta.env.VITE_API_URL}/${id}`);
    if (result.ok) {
      return result.json();
    }
  } catch (err) {
    console.error(err);
    throw new Error("Impossible de récupérer le département");
  }
};

export const updateDepartement = async (nom, id) => {
  try {
    const result = await fetch(`${import.meta.env.VITE_API_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nom }),
    });
    if (result.ok) {
      return result.json();
    }
  } catch (err) {
    console.error(err);
  }
};

export const getDepartement = async () => {
  try {
    const result = await fetch(`${import.meta.env.VITE_API_URL}/`);
    if (result.ok) {
      return result.json();
    }
  } catch (err) {
    console.error(err);
    throw new Error("Impossible de récupérer les départements");
  }
};

export const createDepartement = async (nom) => {
  try {
    const result = await fetch(`${import.meta.env.VITE_API_URL}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nom }),
    });
    if (result.ok) {
      return result.json();
    }
  } catch (err) {
    console.error(err);
  }
};

export const deleteDepartement = async (id) => {
  try {
    const result = await fetch(`${import.meta.env.VITE_API_URL}/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (result.ok) {
      return result.json();
    }
  } catch (err) {
    console.error(err);
  }
};
