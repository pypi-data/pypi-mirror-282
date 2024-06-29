from jaalvarez2818_airport_docs.entities.contact_info import ContactInfo
from jaalvarez2818_airport_docs.entities.flight import Flight
from jaalvarez2818_airport_docs.entities.pax import Pax
from jaalvarez2818_airport_docs.pnl import PNL

if __name__ == '__main__':
    contact_info = ContactInfo(
        contact_name='LAZARO RODRIGUEZ MARTINEZ',
        phone='+5372042621',
        email='control-esp@aerogaviota.avianet.cu'
    )

    flight = Flight(
        flight_number='KG6085',
        flight_type='Charter',
        departure_airport_code='KIN',
        arrival_airport_code='HAV',
        local_departure_date='2024-06-21',
        local_departure_time='15:30',
        local_arrival_date='2024-06-21',
        local_arrival_time='19:20'
    )

    pax_list = [
        Pax(
            first_name='TAYMI', second_name='', last_name='MARTINEZ MENDOZA', gender='F', birth_date='1977-06-01',
            nationality_code='CUB', document_type='P', document_number='L628099', document_expiry_date='2027-12-27',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='ANGEL', second_name='LUIS', last_name='OLIVERA ESCALONA', gender='M', birth_date='1959-03-02',
            nationality_code='CUB', document_type='P', document_number='M070020', document_expiry_date='2028-05-18',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='RODOLFO', second_name='', last_name='VILLAVICENCIO LA O', gender='M', birth_date='1974-12-26',
            nationality_code='CUB', document_type='P', document_number='L646896', document_expiry_date='2028-01-06',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='YERLING', second_name='MARIA', last_name='PULIDO ORIHUELA', gender='F', birth_date='1982-08-17',
            nationality_code='CUB', document_type='P', document_number='E371574', document_expiry_date='2024-06-27',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='KARINA', second_name='RAQUEL', last_name='GARCIA CALDERON', gender='F', birth_date='1969-09-01',
            nationality_code='CUB', document_type='P', document_number='E419207', document_expiry_date='2025-08-14',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='KIRENIA', second_name='', last_name='BATISTA MILIAN', gender='F', birth_date='1979-09-25',
            nationality_code='CUB', document_type='P', document_number='E416300', document_expiry_date='2025-06-09',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='MARIANO', second_name='JESUS', last_name='BERMUDEZ CLEMENTE', gender='M',
            birth_date='1967-04-05',
            nationality_code='CUB', document_type='P', document_number='E421567', document_expiry_date='2025-10-29',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='ANA', second_name='MARY', last_name='NUNEZ PALACIO', gender='F', birth_date='1978-10-11',
            nationality_code='CUB', document_type='P', document_number='E403976', document_expiry_date='2025-08-06',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='JOANNYA', second_name='', last_name='SOL MORENO', gender='F', birth_date='1979-08-05',
            nationality_code='CUB', document_type='P', document_number='E403299', document_expiry_date='2025-08-23',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='JUSTO', second_name='', last_name='NARANJO DEL PINO', gender='M', birth_date='1971-08-29',
            nationality_code='CUB', document_type='P', document_number='E504231', document_expiry_date='2028-08-12',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='Y'
        ),
        Pax(
            first_name='MARICEL', second_name='', last_name='GALIANO DEL CASTILLO', gender='F', birth_date='1969-05-21',
            nationality_code='CUB', document_type='P', document_number='E505669', document_expiry_date='2028-08-30',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='Y'
        ),
        Pax(
            first_name='RELMAN', second_name='RICARDO', last_name='QUINTANA MARTINEZ', gender='M',
            birth_date='1973-02-12',
            nationality_code='CUB', document_type='P', document_number='E399769', document_expiry_date='2026-03-19',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='Y'
        ),
        Pax(
            first_name='MADELEY', second_name='', last_name='MEDINA RODRIGUEZ', gender='F', birth_date='1974-01-07',
            nationality_code='CUB', document_type='P', document_number='E399254', document_expiry_date='2026-07-06',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='Y'
        ),
        Pax(
            first_name='KATIA', second_name='MARIA', last_name='OCHOA AGUILERA', gender='F', birth_date='1970-08-06',
            nationality_code='CUB', document_type='P', document_number='E507578', document_expiry_date='2028-05-10',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='Y'
        ),
        Pax(
            first_name='ERMENGOL', second_name='RAFAEL', last_name='ALMAGUER ARGUELLES', gender='M',
            birth_date='1946-11-03',
            nationality_code='CUB', document_type='P', document_number='K584145', document_expiry_date='2025-12-09',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='ADEL', second_name='MARIO (MENOR)', last_name='DE LA NOVAL PÉREZ', gender='M',
            birth_date='2010-07-29',
            nationality_code='CUB', document_type='P', document_number='L765998', document_expiry_date='2026-09-19',
            document_issuer_code='CUB', origin_code='KIN', destination_code='HAV', flight_class='F'
        ),
        Pax(
            first_name='MIGUEL', second_name='ANTONIO', last_name='CEDENO MERA', gender='M', birth_date='1971-08-17',
            nationality_code='CUB', document_type='P', document_number='L245325', document_expiry_date='2027-05-28',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='REUTILIO', second_name='', last_name='HURTADO PIMENTEL', gender='M', birth_date='1975-04-13',
            nationality_code='CUB', document_type='P', document_number='K755285', document_expiry_date='2026-10-26',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='MAIKEL', second_name='DAVID', last_name='HURTADO GARBEY', gender='M', birth_date='2007-04-20',
            nationality_code='CUB', document_type='P', document_number='K242999', document_expiry_date='2024-11-14',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),

        Pax(
            first_name='MAURO', second_name='DENIS', last_name='HURTADO GARBEY', gender='M', birth_date='2007-04-20',
            nationality_code='CUB', document_type='P', document_number='K242996', document_expiry_date='2024-04-23',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='ANGEL', second_name='PABLO', last_name='CARRALERO DIEGUEZ', gender='M', birth_date='1965-06-07',
            nationality_code='CUB', document_type='P', document_number='N519693', document_expiry_date='2029-06-27',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
        Pax(
            first_name='ISABEL', second_name='MARIA', last_name='VEGA PAVON', gender='F', birth_date='1962-09-25',
            nationality_code='CUB', document_type='P', document_number='N567691', document_expiry_date='2033-08-17',
            document_issuer_code='CUB', origin_code='KIN', destination_code='SCU', flight_class='F'
        ),
    ]

    PNL(contact_info=contact_info, pax_list=pax_list, flight=flight).to_txt()
