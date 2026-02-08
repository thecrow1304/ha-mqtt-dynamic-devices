async function loadDeviceDetails(deviceId) {
  const res = await fetch(`/api/device/${deviceId}`);
  const dev = await res.json();

  document.getElementById("deviceDetails").innerHTML = `
    <h3>Gerätedetails</h3>
    <p><b>Name:</b> ${dev.alias}</p>
    <p><b>Typ:</b> ${dev.type}</p>
    <p><b>Adresse:</b> ${dev.address}</p>
    <p><b>GPS:</b> ${dev.gpsLatitude}, ${dev.gpsLongitude}</p>
  `;
}

 select.onchange = () => {
  loadFields(select.value);
  loadDeviceDetails(select.value);
};

async function loadFields(deviceId) {
  const res = await fetch(`/api/fields/${deviceId}`);
  const fields = await res.json();
  const div = document.getElementById("fields");
  div.innerHTML = "";

  Object.keys(fields).forEach(key => {
    const row = document.createElement("div");
    row.innerHTML = `
      <label>
        <input type="checkbox" checked />
        ${key}
      </label>
    `;
    div.appendChild(row);
  });
}

loadDevices();
