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
	}
});

export default app;