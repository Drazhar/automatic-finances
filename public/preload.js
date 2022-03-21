const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("ipc", {
  getAccounts: () => ipcRenderer.invoke("GET_ACCOUNTS"),
});
