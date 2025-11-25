document.addEventListener("DOMContentLoaded", function () {
  // Detecta la URL actual y añade la clase 'active' al enlace correspondiente
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

  navLinks.forEach((link) => {
    // Obtenemos el href del link (ej: /catequizandos/)
    const linkPath = link.getAttribute("href");

    // Si la URL actual empieza con el link (para que funcione en subpáginas)
    // O si es coincidencia exacta para el Home ('/')
    if (linkPath === "/" && currentPath === "/") {
      link.classList.add("active");
    } else if (linkPath !== "/" && currentPath.startsWith(linkPath)) {
      link.classList.add("active");
    }
  });

  // --- Cierre automático de alertas (Opcional) ---
  // Cierra las alertas de éxito después de 5 segundos
  const alerts = document.querySelectorAll(".alert-success");
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });
});
