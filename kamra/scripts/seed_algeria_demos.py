"""Seed four fictional Algerian hotel scenarios in the isolated staging site.

Synthetic data only. Idempotent per record via stable demo markers.
Run inside the staging backend container:
    bench --site staging.kamra.local execute kamra.scripts.seed_algeria_demos.run
"""

import frappe
from frappe.utils import add_days, date_diff, now_datetime, today


PROPERTIES = [
	{
		"name": "Hôtel El Bahdja",
		"city": "Alger",
		"state": "Alger",
		"address": "12 boulevard Zighoud Youcef, Alger Centre",
		"phone": "+213 21 63 00 00",
		"email": "reservations@elbahdja.example",
		"star": "4 Star",
		"accent": "#0f766e",
		"description": (
			"Hôtel de standing face à la baie d'Alger, à deux pas de la Grande "
			"Poste. Chambres climatisées, restaurant de cuisine algérienne et "
			"terrasse panoramique sur la Méditerranée."
		),
		"amenities": "Wi-Fi, Restaurant, Terrasse, Parking, Réception 24h/24, Navette aéroport",
		"slug": "elb",
		"types": [
			("STD", "Chambre Classique Vue Ville", 14500, 2, 1, "Double", "Vue ville", 2),
			("DLX", "Chambre Deluxe Vue Mer", 22500, 2, 1, "King", "Vue mer", 2),
			("JSU", "Junior Suite Bahdja", 34000, 3, 2, "King", "Vue mer", 2),
		],
		"guests": [
			("Amina", "Benkhelifa", "Algerian", "Alger", "F", 0),
			("Yacine", "Boudiaf", "Algerian", "Blida", "M", 0),
			("Leïla", "Mansouri", "Algerian", "Oran", "F", 1),
			("Karim", "Zeroual", "Algerian", "Alger", "M", 0),
			("Nadia", "Hamdi", "Algerian", "Constantine", "F", 0),
			("Sofiane", "Belkacem", "Algerian", "Tizi Ouzou", "M", 0),
			("Claire", "Dubois", "French", "Paris", "F", 0),
			("Marco", "Rossi", "Italian", "Milan", "M", 0),
		],
		"reservations": [
			("R1", "Checked In", -2, 1, "STD", 0, 2, 0, "Website", "", "MAP", 0),
			("R2", "Checked In", -1, 2, "DLX", 0, 2, 1, "OTA", "Booking.com", "MAP", 1),
			("R3", "Confirmed", 0, 3, "STD", 1, 1, 0, "Phone", "", "EP", 2),
			("R4", "Confirmed", 0, 2, "JSU", 0, 2, 0, "Walk-in", "", "MAP", 3),
			("R5", "Confirmed", 5, 8, "DLX", 1, 2, 0, "Website", "", "EP", 4),
			("R6", "Checked Out", -5, -2, "STD", 1, 2, 0, "Manual", "", "EP", 5),
			("R7", "Cancelled", 1, 3, "JSU", None, 2, 0, "Phone", "", "EP", 6),
			("R8", "No Show", -1, 1, "STD", None, 1, 0, "OTA", "Expedia", "EP", 7),
		],
	},
	{
		"name": "Dar Cirta Boutique Hotel",
		"city": "Constantine",
		"state": "Constantine",
		"address": "8 rue Larbi Ben M'hidi, Constantine",
		"phone": "+213 31 92 00 00",
		"email": "contact@darcirta.example",
		"star": "Boutique",
		"accent": "#9a3412",
		"description": (
			"Maison de caractère perchée au-dessus des gorges du Rhumel. "
			"Neuf chambres restaurées, patio andalou et table d'hôtes "
			"autour des spécialités constantinoises."
		),
		"amenities": "Wi-Fi, Patio, Table d'hôtes, Bibliothèque, Vue gorges, Conciergerie",
		"slug": "cir",
		"types": [
			("CLS", "Chambre Classique Patio", 18500, 2, 1, "Queen", "Patio", 2),
			("PST", "Suite Pont Sidi M'Cid", 32000, 3, 1, "King", "Gorges du Rhumel", 2),
			("TRC", "Chambre Terrasse", 24500, 2, 1, "Double", "Vue médina", 2),
		],
		"guests": [
			("Samir", "Bensalem", "Algerian", "Constantine", "M", 0),
			("Yasmine", "Khelifi", "Algerian", "Alger", "F", 0),
			("Nour El Houda", "Saadi", "Algerian", "Constantine", "F", 1),
			("Adel", "Boudjema", "Algerian", "Sétif", "M", 0),
			("Meriem", "Larbi", "Algerian", "Annaba", "F", 0),
			("Walid", "Benabbas", "Algerian", "Constantine", "M", 0),
			("Elena", "García", "Spanish", "Madrid", "F", 0),
			("Thomas", "Müller", "German", "Berlin", "M", 0),
		],
		"reservations": [
			("R1", "Checked In", -2, 1, "CLS", 0, 2, 0, "Phone", "", "MAP", 0),
			("R2", "Checked In", -1, 2, "PST", 0, 2, 1, "Website", "", "MAP", 1),
			("R3", "Confirmed", 0, 3, "CLS", 1, 1, 0, "OTA", "Booking.com", "EP", 2),
			("R4", "Confirmed", 0, 2, "TRC", 0, 2, 0, "Walk-in", "", "MAP", 3),
			("R5", "Confirmed", 5, 8, "PST", 1, 2, 0, "Website", "", "EP", 4),
			("R6", "Checked Out", -5, -2, "CLS", 1, 2, 0, "Manual", "", "EP", 5),
			("R7", "Cancelled", 1, 3, "TRC", None, 2, 0, "Phone", "", "EP", 6),
			("R8", "No Show", -1, 1, "CLS", None, 1, 0, "OTA", "Expedia", "EP", 7),
		],
	},
	{
		"name": "Hôtel Cap Gouraya",
		"city": "Béjaïa",
		"state": "Béjaïa",
		"address": "Route de la Corniche, Aiguades, Béjaïa",
		"phone": "+213 34 21 00 00",
		"email": "reservation@capgouraya.example",
		"star": "4 Star",
		"accent": "#1d4ed8",
		"description": (
			"Hôtel familial les pieds dans l'eau, à l'ombre du mont Gouraya. "
			"Chambres ouvertes sur la Méditerranée, piscine et restaurant "
			"de poisson grillé sur la plage."
		),
		"amenities": "Wi-Fi, Piscine, Plage privée, Restaurant, Parking, Sports nautiques",
		"slug": "gou",
		"types": [
			("SVD", "Chambre Double Vue Mer", 16500, 2, 1, "Double", "Vue mer", 2),
			("FAM", "Suite Familiale Gouraya", 29500, 4, 2, "Twin", "Vue mer", 2),
			("BNG", "Bungalow Jardin", 21000, 2, 1, "Queen", "Jardin", 2),
		],
		"guests": [
			("Lina", "Aït Ali", "Algerian", "Béjaïa", "F", 0),
			("Massinissa", "Amrouche", "Algerian", "Tizi Ouzou", "M", 0),
			("Kahina", "Brahimi", "Algerian", "Béjaïa", "F", 1),
			("Younes", "Ouali", "Algerian", "Alger", "M", 0),
			("Thiziri", "Idir", "Algerian", "Bouira", "F", 0),
			("Farid", "Khelfaoui", "Algerian", "Sétif", "M", 0),
			("Sofia", "Marchetti", "Italian", "Rome", "F", 0),
			("Paul", "Lefèvre", "French", "Lyon", "M", 0),
		],
		"reservations": [
			("R1", "Checked In", -2, 1, "SVD", 0, 2, 0, "Website", "", "MAP", 0),
			("R2", "Checked In", -1, 2, "FAM", 0, 2, 2, "OTA", "Booking.com", "MAP", 1),
			("R3", "Confirmed", 0, 3, "SVD", 1, 1, 0, "Phone", "", "EP", 2),
			("R4", "Confirmed", 0, 2, "BNG", 0, 2, 0, "Walk-in", "", "MAP", 3),
			("R5", "Confirmed", 5, 8, "FAM", 1, 2, 1, "Website", "", "EP", 4),
			("R6", "Checked Out", -5, -2, "SVD", 1, 2, 0, "Manual", "", "EP", 5),
			("R7", "Cancelled", 1, 3, "BNG", None, 2, 0, "Phone", "", "EP", 6),
			("R8", "No Show", -1, 1, "SVD", None, 1, 0, "OTA", "Expedia", "EP", 7),
		],
	},
	{
		"name": "Maison du M'Zab",
		"city": "Ghardaïa",
		"state": "Ghardaïa",
		"address": "Quartier historique de Beni Isguen, Ghardaïa",
		"phone": "+213 29 87 00 00",
		"email": "accueil@maisonmzab.example",
		"star": "Boutique",
		"accent": "#b45309",
		"description": (
			"Maison d'hôtes en terre ocre au cœur de la vallée du M'Zab. "
			"Chambres voûtées, cour fraîche, dattes et thé à la menthe, "
			"à quelques pas des remparts de Beni Isguen."
		),
		"amenities": "Wi-Fi, Cour intérieure, Terrasse, Petit-déjeuner, Visites guidées, Artisanat",
		"slug": "mzb",
		"types": [
			("CRY", "Chambre Courtyard", 13500, 2, 1, "Double", "Cour intérieure", 2),
			("OCS", "Suite Ocre", 24000, 3, 1, "King", "Vue ksar", 2),
			("RFT", "Chambre Toit-Terrasse", 18000, 2, 1, "Queen", "Vue vallée", 2),
		],
		"guests": [
			("Fatiha", "Beni Moussa", "Algerian", "Ghardaïa", "F", 0),
			("Brahim", "Ould Kacem", "Algerian", "Ghardaïa", "M", 0),
			("Zineb", "Belaid", "Algerian", "Alger", "F", 1),
			("Mokhtar", "Hadj Said", "Algerian", "El Oued", "M", 0),
			("Aïcha", "Benamar", "Algerian", "Ghardaïa", "F", 0),
			("Rachid", "Benslimane", "Algerian", "Laghouat", "M", 0),
			("Hélène", "Moreau", "French", "Bordeaux", "F", 0),
			("David", "Klein", "German", "Hamburg", "M", 0),
		],
		"reservations": [
			("R1", "Checked In", -2, 1, "CRY", 0, 2, 0, "Website", "", "MAP", 0),
			("R2", "Checked In", -1, 2, "OCS", 0, 2, 1, "Phone", "", "MAP", 1),
			("R3", "Confirmed", 0, 3, "CRY", 1, 1, 0, "OTA", "Booking.com", "EP", 2),
			("R4", "Confirmed", 0, 2, "RFT", 0, 2, 0, "Walk-in", "", "MAP", 3),
			("R5", "Confirmed", 5, 8, "OCS", 1, 2, 0, "Website", "", "EP", 4),
			("R6", "Checked Out", -5, -2, "CRY", 1, 2, 0, "Manual", "", "EP", 5),
			("R7", "Cancelled", 1, 3, "RFT", None, 2, 0, "Phone", "", "EP", 6),
			("R8", "No Show", -1, 1, "CRY", None, 1, 0, "OTA", "Expedia", "EP", 7),
		],
	},
]


def _ascii(value):
	import unicodedata
	return (
		unicodedata.normalize("NFKD", value)
		.encode("ascii", "ignore")
		.decode("ascii")
		.lower()
		.replace(" ", ".")
		.replace("'", "")
	)


def ensure_property(spec):
	name = spec["name"]
	if frappe.db.exists("Property", name):
		return frappe.get_doc("Property", name)
	return frappe.get_doc({
		"doctype": "Property",
		"property_name": name,
		"legal_name": name + " SARL",
		"property_kind": "Hotel",
		"phone": spec["phone"],
		"email": spec["email"],
		"website": "https://" + spec["slug"] + ".example",
		"address_line": spec["address"],
		"city": spec["city"],
		"state": spec["state"],
		"country": "Algeria",
		"pincode": "16000" if spec["city"] == "Alger" else "25000" if spec["city"] == "Constantine" else "06000" if spec["city"] == "Béjaïa" else "47000",
		"timezone": "Africa/Algiers",
		"currency": "DZD",
		"locale": "fr",
		"checkin_time": "14:00:00",
		"checkout_time": "12:00:00",
		"minimum_nights": 1,
		"booking_mode": "Instant",
		"star_category": spec["star"],
		"brand_accent": spec["accent"],
		"showcase_description": spec["description"],
		"property_amenities": spec["amenities"],
		"privacy_contact": "privacy@" + spec["slug"] + ".example",
		"guest_retention_months": 24,
		"free_cancel_days": 2,
		"cancellation_fee": "First Night",
		"no_show_charge": "First Night",
		"room_levy_label": "Taxe de séjour",
		"room_levy_mode": "Fixed per person per night",
		"room_levy_amount": 100,
		"room_levy_taxable": 0,
		"rates_include_tax": 0,
		"gst_mode": "Fixed",
		"gst_rate_low": 9,
		"gst_rate_high": 9,
		"booking_engine_enabled": 0,
		"disabled": 0,
	}).insert(ignore_permissions=True)


def ensure_room_types(spec):
	out = {}
	for code, label, price, adults, children, bed, view, count in spec["types"]:
		name = f"{spec['name']}-{code}"
		if not frappe.db.exists("Room Type", name):
			frappe.get_doc({
				"doctype": "Room Type",
				"property": spec["name"],
				"room_type_code": code,
				"room_type_name": label,
				"room_category": "Private",
				"description": f"{label} — données de démonstration synthétiques.",
				"base_price": price,
				"base_occupancy": adults,
				"single_occupancy_price": price * 0.8,
				"extra_adult_price": price * 0.2,
				"extra_bed_price": 3500,
				"max_extra_beds": 1,
				"free_child_age": 6,
				"child_age_limit": 12,
				"child_price": price * 0.35,
				"adults_capacity": adults,
				"children_capacity": children,
				"max_total_occupants": adults + children,
				"bed_type": bed,
				"room_view": view,
				"smoking_allowed": 0,
				"air_conditioning": "AC",
				"bathroom": "Attached",
				"amenities": "Wi-Fi, Climatisation, Salle de bain privée, Coffre-fort, TV",
				"tax_percent": 9,
				"disabled": 0,
			}).insert(ignore_permissions=True)
		out[code] = frappe.get_doc("Room Type", name)
	return out


def ensure_rooms(spec, types):
	rooms = {}
	for t_idx, (code, room_type) in enumerate(types.items()):
		for idx, number in enumerate((f"{t_idx + 1}01", f"{t_idx + 1}02")):
			name = f"{spec['name']}-{number}"
			if not frappe.db.exists("Room", name):
				frappe.get_doc({
					"doctype": "Room",
					"property": spec["name"],
					"room_number": number,
					"room_type": room_type.name,
					"floor": number[0],
					"housekeeping_status": "Clean",
					"occupancy_status": "Vacant",
					"notes": "Chambre de démonstration — données synthétiques.",
				}).insert(ignore_permissions=True)
			rooms[(code, idx)] = frappe.get_doc("Room", name)
	return rooms


def ensure_plans(spec):
	rate_name = f"{spec['name']}-BAR"
	if not frappe.db.exists("Rate Plan", rate_name):
		frappe.get_doc({
			"doctype": "Rate Plan",
			"property": spec["name"],
			"rate_plan_name": "Best Available Rate",
			"code": "BAR",
			"modifier_type": "Percent",
			"modifier_value": 0,
			"is_default": 1,
			"cancellation_policy": "Annulation gratuite jusqu'à 48 h avant l'arrivée.",
			"disabled": 0,
		}).insert(ignore_permissions=True)
	plans = {}
	for code, label, adult, child in (
		("EP", "Chambre seule", 0, 0),
		("MAP", "Demi-pension", 2800, 1400),
	):
		name = f"{spec['name']}-{code}"
		if not frappe.db.exists("Meal Plan", name):
			frappe.get_doc({
				"doctype": "Meal Plan",
				"property": spec["name"],
				"code": code,
				"label": label,
				"price_per_adult": adult,
				"price_per_child": child,
				"is_default": 1 if code == "EP" else 0,
				"disabled": 0,
			}).insert(ignore_permissions=True)
		plans[code] = name
	plans["BAR"] = rate_name
	return plans


def ensure_guests(spec):
	guests = []
	for idx, (first, last, nationality, city, gender, vip) in enumerate(spec["guests"], start=1):
		email = f"{_ascii(first)}.{_ascii(last)}@{spec['slug']}.example"
		name = frappe.db.get_value("Guest", {"email": email})
		if not name:
			name = frappe.get_doc({
				"doctype": "Guest",
				"first_name": first,
				"last_name": last,
				"full_name": f"{first} {last}",
				"phone": f"+213 5{idx:02d} {idx:02d} {idx:02d} {idx:02d}",
				"email": email,
				"nationality": nationality,
				"city": city,
				"address_line": f"Adresse de démonstration {idx}, {city}",
				"guest_category": "VIP" if vip else "Standard",
				"vip": vip,
				"id_type": "Passport" if nationality != "Algerian" else "Carte d'identité",
				"id_number": f"DEMO-{spec['slug'].upper()}-{idx:03d}",
				"gender": "Female" if gender == "F" else "Male",
				"guest_notes": "Profil de démonstration — données synthétiques, aucune personne réelle.",
			}).insert(ignore_permissions=True).name
		guests.append(frappe.get_doc("Guest", name))
	return guests


def _set_amounts(res, nights, base_price):
	before = float(base_price) * max(1, nights)
	tax = round(before * 0.09, 2)
	res.amount_before_tax = before
	res.tax_amount = tax
	res.amount_after_tax = before + tax


def ensure_reservations(spec, types, rooms, plans, guests):
	for (key, status, ci_off, co_off, type_code, room_idx, adults, children,
	     source, channel, meal_code, guest_idx) in spec["reservations"]:
		marker = f"DEMO-{spec['slug'].upper()}-{key}"
		if frappe.db.exists("Reservation", {"ota_ref": marker}):
			continue
		ci = add_days(today(), ci_off)
		co = add_days(today(), co_off)
		guest = guests[guest_idx]
		room_type = types[type_code]
		room = rooms[(type_code, room_idx)] if room_idx is not None else None
		nights = max(1, date_diff(co, ci))
		res = frappe.get_doc({
			"doctype": "Reservation",
			"property": spec["name"],
			"guest": guest.name,
			"guest_name": guest.full_name,
			"status": status,
			"source": source,
			"channel": channel,
			"ota_ref": marker,
			"idempotency_key": marker.lower(),
			"room_type": room_type.name,
			"room": room.name if room else None,
			"check_in_date": ci,
			"check_out_date": co,
			"nights": nights,
			"adults": adults,
			"children": children,
			"booking_type": "Individual",
			"meal_plan": plans[meal_code],
			"rate_plan": plans["BAR"],
			"auto_price": 0,
			"is_pay_at_hotel": 1,
			"advance_paid": 0,
			"planned_check_in_time": "15:00:00",
			"planned_check_out_time": "11:00:00",
			"eta": "15:00",
			"purpose": "Leisure" if guest_idx % 2 == 0 else "Business",
			"special_requests": "Lit bébé" if children else "Chambre calme, si possible",
			"booked_by_name": guest.full_name,
			"booked_by_phone": guest.phone,
			"booker_relation": "Family" if children else "Other",
			"contact_preference": "Guest",
			"arrival_mode": "Air" if guest_idx % 3 == 0 else "Road",
			"arrival_ref": f"AH {1000 + guest_idx}" if guest_idx % 3 == 0 else "",
			"departure_mode": "Air" if guest_idx % 3 == 0 else "Road",
			"departure_ref": f"AH {2000 + guest_idx}" if guest_idx % 3 == 0 else "",
			"cancellation_reason": "Change of plans" if status == "Cancelled" else None,
			"cancellation_note": "Annulation de démonstration." if status == "Cancelled" else None,
		})
		_set_amounts(res, nights, room_type.base_price)
		res.flags.allow_past_check_in = True
		res.insert(ignore_permissions=True)

		if status in ("Checked In", "Checked Out"):
			# Post the nights already consumed so the open folio is not empty.
			from kamra.folio import post_room_night
			consumed = date_diff(today(), ci)
			for offset in range(max(0, min(consumed, nights))):
				post_room_night(res, add_days(ci, offset))
			folio_name = frappe.db.get_value(
				"Folio", {"reservation": res.name, "folio_type": "Guest"})
			if folio_name:
				from kamra.folio import _recalculate, close_folio
				folio = frappe.get_doc("Folio", folio_name)
				paid = float(folio.grand_total) if status == "Checked Out" else round(float(folio.grand_total) * 0.5, 2)
				if paid:
					folio.append("payments", {
						"posting_date": today(),
						"payment_kind": "Payment",
						"mode": "Card" if key == "R1" else "Cash",
						"amount": paid,
						"reference": f"DEMO-PAY-{spec['slug'].upper()}-{key}",
					})
					_recalculate(folio)
					folio.save(ignore_permissions=True)
				if status == "Checked Out":
					try:
						close_folio(folio_name)
					except Exception as exc:
						print("close_folio skipped", res.name, repr(exc))
			if status == "Checked Out":
				res.db_set("actual_check_in", add_days(ci, 0).__str__() + " 15:00:00", update_modified=False)
				res.db_set("actual_check_out", add_days(co, 0).__str__() + " 11:00:00", update_modified=False)

		if status == "Checked In":
			res.db_set("actual_check_in", add_days(ci, 0).__str__() + " 15:00:00", update_modified=False)


def ensure_housekeeping(spec, rooms, types):
	type_codes = list(types.keys())
	tasks = [
		((type_codes[1], 0), "Stayover Clean", "Medium", "In Progress", "Nettoyage de séjour — démonstration."),
		((type_codes[2], 0), "Deep Clean", "High", "Pending", "Remise en état — démonstration."),
		((type_codes[2], 1), "Inspection", "Low", "Pending", "Contrôle qualité — démonstration."),
	]
	for (type_code, idx), task_type, priority, status, notes in tasks:
		room = rooms[(type_code, idx)]
		if frappe.db.exists("Housekeeping Task", {"property": spec["name"], "room": room.name, "notes": notes}):
			continue
		frappe.get_doc({
			"doctype": "Housekeeping Task",
			"property": spec["name"],
			"room": room.name,
			"task_type": task_type,
			"priority": priority,
			"status": status,
			"assigned_to_user": "hk@ziri.local",
			"assignment_status": "Assigned",
			"notes": notes,
		}).insert(ignore_permissions=True)


def repair_room_states(spec, rooms, types):
	"""Make the operational picture coherent after a bulk seed.

	Reservation.on_update does not run its check-in/check-out side effects
	for a brand-new document, so set the room board and the checkout task
	explicitly. This is presentation data for the demo, not a product path.
	"""
	type_codes = list(types.keys())
	occupied = set()
	for res in frappe.get_all(
		"Reservation",
		filters={"property": spec["name"], "status": "Checked In"},
		fields=["name", "room"],
	):
		if not res.room:
			continue
		occupied.add(res.room)
		frappe.db.set_value("Room", res.room, {
			"occupancy_status": "Occupied",
			"housekeeping_status": "Clean",
		})
		# Today's room + meal charges make the dashboard's revenue tile real.
		from kamra.folio import post_room_night
		post_room_night(frappe.get_doc("Reservation", res.name), today())

	for res in frappe.get_all(
		"Reservation",
		filters={"property": spec["name"], "status": "Checked Out"},
		fields=["name", "room"],
	):
		if not res.room:
			continue
		frappe.db.set_value("Room", res.room, {
			"occupancy_status": "Vacant",
			"housekeeping_status": "Inspected",
		})
		if not frappe.db.exists(
			"Housekeeping Task",
			{"property": spec["name"], "room": res.room, "reservation": res.name},
		):
			frappe.get_doc({
				"doctype": "Housekeeping Task",
				"property": spec["name"],
				"room": res.room,
				"task_type": "Checkout Clean",
				"priority": "High",
				"status": "Done",
				"reservation": res.name,
				"assigned_to_user": "hk@ziri.local",
				"assignment_status": "Assigned",
				"notes": "Nettoyage de départ terminé — démonstration.",
			}).insert(ignore_permissions=True)

	for (type_code, idx), state in (
		((type_codes[2], 0), "Dirty"),
		((type_codes[2], 1), "Inspected"),
		((type_codes[1], 1), "Clean"),
	):
		room = rooms[(type_code, idx)]
		if room.name not in occupied:
			frappe.db.set_value("Room", room.name, "housekeeping_status", state)


CONFIRMATION = "SEED_SYNTHETIC_DEMO_DATA"


def run(confirm: str | None = None):
	"""Create the four fictional demo properties on the current site.

	Deliberately refuses to run without an explicit confirmation token: this
	writes sample properties, rooms, guests and reservations, and a mistyped
	`bench --site` must not be able to add them to a live hotel.
	"""
	if confirm != CONFIRMATION:
		frappe.throw(
			"Refusing to seed demo data. Re-run against an isolated staging "
			f"site with confirm='{CONFIRMATION}'."
		)
	frappe.set_user("Administrator")  # nosemgrep: frappe-setuser -- bench-execute seeder; the confirm token above gates it and the caller already holds bench shell access
	for spec in PROPERTIES:
		print("===", spec["name"])
		ensure_property(spec)
		types = ensure_room_types(spec)
		rooms = ensure_rooms(spec, types)
		plans = ensure_plans(spec)
		guests = ensure_guests(spec)
		ensure_reservations(spec, types, rooms, plans, guests)
		ensure_housekeeping(spec, rooms, types)
		repair_room_states(spec, rooms, types)
		frappe.db.commit()  # nosemgrep: frappe-manual-commit -- commits each demo property as it is built, so a failed later property cannot discard the earlier ones
		print("rooms", frappe.db.count("Room", {"property": spec["name"]}),
		      "guests ok", len(guests),
		      "reservations", frappe.db.count("Reservation", {"property": spec["name"]}))
	print("done")
