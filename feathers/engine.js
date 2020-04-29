const electron = require('electron');
const path = require('path');
const url = require('url');

process.env.NODE_ENV = "development";

const { app: sterling, BrowserWindow, Menu, ipcMain } = electron;

const developer = true;

const sterling_menu_template = [{
	label: 'Edit',
	submenu: [
		{ role: 'undo' },
		{ role: 'redo' },
		{ role: 'cut' },
		{ role: 'copy' },
		{ role: 'paste' }
	]
}];

let sterling_ui;

function build_menu() {

	if (process.platform == 'darwin') sterling_menu_template.unshift({
		label: sterling.getName(),
		submenu: [
			{ role: 'about' },
			{ role: 'hide' },
			{ role: 'unhide' },
			{ role: 'quit' }
		]
	});

	if (process.env.NODE_ENV !== 'production') sterling_menu_template.push({
		label: 'Developer Tools',
		submenu: [
			{ role: 'reload' },
			{ role: 'toggledevtools' }
		]
	});

	const main_menu = Menu.buildFromTemplate(sterling_menu_template);

	Menu.setApplicationMenu(main_menu);
}

function init_sterling() {

	sterling.setName('Sterling');

	sterling_ui = new BrowserWindow({
		width: 960,
		height: 700,
		minWidth: 780,
		minHeight: 500,
		kiosk: false,
		title: "Sterling",
		frame: (process.platform == 'darwin') ? true : false,
		titleBarStyle: (process.platform == 'darwin') ? 'hiddenInset' : '',
		show: false,
		webPreferences: {
			devTools: developer,
			nodeIntegration: false,
			contextIsolation: true,
			safeDialogs: true,
			preload: 'preload.js'
		}
	});

	build_menu();

	sterling_ui.loadURL(url.format({

		pathname: path.join(__dirname, 'view/home.html'),
		protocol: 'file:',
		slashes: true
	}));

	sterling_ui.once('ready-to-show', () => { sterling_ui.show(); });
	sterling_ui.on('closed', quit_sterling);
}

function quit_sterling() {
	sterling.quit();
}

sterling.on('ready', init_sterling);
sterling.on('window-all-closed', quit_sterling);