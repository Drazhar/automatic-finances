import { ipcMain } from "electron";

import * as db from "./sqlite.js";

export default function defineIpcHandles() {
  ipcMain.handle("GET_ACCOUNTS", db.getAccounts);
}
