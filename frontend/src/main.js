import App from './App.svelte';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';

const app = new App({
	target: document.body,
	props: {
		base_url: 'web:8000',
		fractions: [
			{
				"id": 1,
				"material": "Пластик",
			},
			{
				"id": 2,
				"material": "Металл",
			},
			{
				"id": 3,
				"material": "Бумага",
			},
			{
				"id": 4,
				"material": "Стекло",
			},
			{
				"id": 5,
				"material": "Одежда",
			},
			{
				"id": 6,
				"material": "Батарейки",
			},
			{
				"id": 7,
				"material": "Лампочки",
			},
			{
				"id": 8,
				"material": "Техника",
			},
			{
				"id": 9,
				"material": "Крышечки",
			},
			{
				"id": 10,
				"material": "Шины",
			},
			{
				"id": 11,
				"material": "Зубные щётки",
			},{
				"id": 12,
				"material": "Градусники",
			},
			{
				"id": 13,
				"material": "Иное",
			}
		],
		markings: [
			{'id': 1, 'type': 'PET 01'},
			{'id': 1, 'type': 'PET 1'},
			{'id': 1, 'type': 'PET'},
			{'id': 1, 'type': '01'},
			{'id': 1, 'type': '1'},
			{'id': 1, 'type': 'HDPE 02'},
			{'id': 1, 'type': 'HDPE 2'},
			{'id': 1, 'type': 'HDPE'},
			{'id': 1, 'type': '02'},
			{'id': 1, 'type': '2'},
			{'id': 1, 'type': 'LDPE 04'},
			{'id': 1, 'type': 'LDPE 4'},
			{'id': 1, 'type': 'LDPE'},
			{'id': 1, 'type': '04'},
			{'id': 1, 'type': '4'},
			{'id': 1, 'type': 'PP 05'},
			{'id': 1, 'type': 'PP 5'},
			{'id': 1, 'type': 'PP'},
			{'id': 1, 'type': '05'},
			{'id': 1, 'type': '5'},
			{'id': 1, 'type': 'PS 06'},
			{'id': 1, 'type': 'PS 6'},
			{'id': 1, 'type': 'PS'},
			{'id': 1, 'type': '06'},
			{'id': 1, 'type': '6'},
			{'id': 2, 'type': 'FE 40'},
			{'id': 2, 'type': 'FE'},
			{'id': 2, 'type': '40'},
			{'id': 2, 'type': 'ALU 41'},
			{'id': 2, 'type': 'ALU'},
			{'id': 2, 'type': '41'},
			{'id': 3, 'type': 'PAP 20'},
			{'id': 3, 'type': 'PAP'},
			{'id': 3, 'type': '20'},
			{'id': 3, 'type': 'PAP 21'},
			{'id': 3, 'type': '21'},
			{'id': 3, 'type': 'PAP 22'},
			{'id': 3, 'type': '22'},
			{'id': 4, 'type': 'GL 70'},
			{'id': 4, 'type': 'GL'},
			{'id': 4, 'type': '70'},
			{'id': 4, 'type': 'GL 71'},
			{'id': 4, 'type': '71'},
			{'id': 4, 'type': 'GL 72'},
			{'id': 4, 'type': '72'},
			{'id': 4, 'type': 'GLS 73'},
			{'id': 4, 'type': 'GLS'},
			{'id': 4, 'type': '73'},
			{'id': 4, 'type': 'GLS 74'},
			{'id': 4, 'type': '74'},
			{'id': 14, 'type': 'PVC 03'},
			{'id': 14, 'type': 'PVC 3'},
			{'id': 14, 'type': 'PVC'},
			{'id': 14, 'type': '03'},
			{'id': 14, 'type': '3'},
			{'id': 14, 'type': 'OTHER 07'},
			{'id': 14, 'type': 'OTHER 7'},
			{'id': 14, 'type': 'OTHER'},
			{'id': 14, 'type': '07'},
			{'id': 14, 'type': '7'},
			{'id': 14, 'type': 'C/PP'},
			{'id': 14, 'type': 'C/LDPE'}
		]
	}
});

export default app;