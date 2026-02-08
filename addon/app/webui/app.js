async function loadDevices() {
  const res = await fetch("/api/devices");
  const devices = await res.json();
  const select = document.getElementById("deviceSelect");

  Object.entries(devices).forEach(([id, dev]) => {
    const opt = document.createElement("option");
    opt.value = id;
    opt.text = dev.alias || id;
    select.appendChild(opt);
  });

  select.onchange = () => loadFields(select.value);
}

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
