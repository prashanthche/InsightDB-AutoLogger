def insert_fake_web_visitor():
    conn = get_connection()
    cur = conn.cursor()
    fake = Faker()

    ip = fake.ipv4()
    device = fake.user_agent()[:490]  # safely trim long values
    referrer = fake.url()
    now = datetime.now()

    cur.execute("""
        INSERT INTO web_visitors (visited_at, ip_address, device, referrer)
        VALUES (%s, %s, %s, %s);
    """, (now, ip, device, referrer))

    conn.commit()
    cur.close()
    conn.close()
