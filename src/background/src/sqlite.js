const sqlite3 = require("sqlite3").verbose();
const path = require("path");
import { app } from "electron";

const db = new sqlite3.Database(
  path.join(app.getPath("userData"), "financeData.db")
);

export function initialize() {
  db.serialize(() => {
    db.run(
      `
    CREATE TABLE IF NOT EXISTS accounts (
      name VARCHAR(255) NOT NULL,
      currency VARCHAR(3) NOT NULL,
      type INT NOT NULL
    );`
    );
  });
}

export async function addAccount(name, currency, type) {
  return new Promise((resolve, reject) => {
    db.run(
      `INSERT INTO accounts (name, currency, type)
            VALUES ("${name}", "${currency}", ${type})`,
      function (err) {
        if (err) {
          reject(err);
        } else {
          resolve(this.changes);
        }
      }
    );
  });
}

export async function deleteAccount(id) {
  return new Promise((resolve, reject) => {
    db.run(
      `DELETE FROM accounts
       WHERE rowid = ${id}`,
      function (err) {
        if (err) {
          reject(err);
        } else {
          resolve({
            lastID: this.lastID,
            changes: this.changes,
          });
        }
      }
    );
  });
}

export async function getAccounts() {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT rowid as id, name, currency, type
       FROM accounts`,
      function (err, rows) {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      }
    );
  });
}
