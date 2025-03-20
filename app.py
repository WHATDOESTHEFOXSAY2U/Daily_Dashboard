import os
os.environ["WANDB_API_KEY"] = "dc8365dbf9d140e05fd56f6f68afa031b44ae637"

import streamlit as st
import datetime
import pandas as pd
import altair as alt

def init_states():
    if "kpi_history" not in st.session_state:
        st.session_state["kpi_history"] = []
    if "kpis" not in st.session_state:
        st.session_state["kpis"] = default_kpis()
    if "selected_date" not in st.session_state:
        st.session_state["selected_date"] = datetime.date.today()
    if "pay_data" not in st.session_state:
        st.session_state["pay_data"] = full_pay_data()

def default_kpis():
    return {
        "scotiaBank": False,
        "rakutenRewards": False,
        "workout": False,
        "onlineBusiness": False,
        "approaches": 0,
        "emailOutreach": False
    }

def full_pay_data():
    return {
        "months": [
            {
                "id": "feb-2025","name": "February","year": 2025,
                "paychecks": [
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Feb 6","isoDate":"2025-02-06","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Feb 20","isoDate":"2025-02-20","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"Feb 14","isoDate":"2025-02-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"Feb 28","isoDate":"2025-02-28","amount":4200,"received":False}
                ]
            },
            {
                "id": "mar-2025","name":"March","year":2025,
                "paychecks": [
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Mar 6","isoDate":"2025-03-06","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Mar 20","isoDate":"2025-03-20","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"Mar 14","isoDate":"2025-03-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"Mar 28","isoDate":"2025-03-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"apr-2025","name":"April","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Apr 3","isoDate":"2025-04-03","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Apr 17","isoDate":"2025-04-17","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"Apr 14","isoDate":"2025-04-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"Apr 28","isoDate":"2025-04-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"may-2025","name":"May","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"May 1","isoDate":"2025-05-01","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"May 15","isoDate":"2025-05-15","amount":2200,"received":False},
                    {"id":"scotia-3","type":"scotia","name":"Scotia Bank","displayDate":"May 29","isoDate":"2025-05-29","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"May 14","isoDate":"2025-05-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"May 28","isoDate":"2025-05-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"jun-2025","name":"June","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Jun 12","isoDate":"2025-06-12","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Jun 26","isoDate":"2025-06-26","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"Jun 14","isoDate":"2025-06-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"Jun 28","isoDate":"2025-06-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"jul-2025","name":"July","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Jul 10","isoDate":"2025-07-10","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Jul 24","isoDate":"2025-07-24","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-07-14","isoDate":"2025-07-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-07-28","isoDate":"2025-07-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"aug-2025","name":"August","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Aug 7","isoDate":"2025-08-07","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Aug 21","isoDate":"2025-08-21","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-08-14","isoDate":"2025-08-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-08-28","isoDate":"2025-08-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"sep-2025","name":"September","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Sep 4","isoDate":"2025-09-04","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Sep 18","isoDate":"2025-09-18","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-09-14","isoDate":"2025-09-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-09-28","isoDate":"2025-09-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"oct-2025","name":"October","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Oct 2","isoDate":"2025-10-02","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Oct 16","isoDate":"2025-10-16","amount":2200,"received":False},
                    {"id":"scotia-3","type":"scotia","name":"Scotia Bank","displayDate":"Oct 30","isoDate":"2025-10-30","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-10-14","isoDate":"2025-10-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-10-28","isoDate":"2025-10-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"nov-2025","name":"November","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"Nov 13","isoDate":"2025-11-13","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"Nov 27","isoDate":"2025-11-27","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-11-14","isoDate":"2025-11-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-11-28","isoDate":"2025-11-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"dec-2025","name":"December","year":2025,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"2025-12-11","isoDate":"2025-12-11","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"2025-12-25","isoDate":"2025-12-25","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2025-12-14","isoDate":"2025-12-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2025-12-28","isoDate":"2025-12-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"jan-2026","name":"January","year":2026,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"2026-01-08","isoDate":"2026-01-08","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"2026-01-22","isoDate":"2026-01-22","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2026-01-14","isoDate":"2026-01-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2026-01-28","isoDate":"2026-01-28","amount":4200,"received":False}
                ]
            },
            {
                "id":"feb-2026","name":"February","year":2026,
                "paychecks":[
                    {"id":"scotia-1","type":"scotia","name":"Scotia Bank","displayDate":"2026-02-05","isoDate":"2026-02-05","amount":2200,"received":False},
                    {"id":"scotia-2","type":"scotia","name":"Scotia Bank","displayDate":"2026-02-19","isoDate":"2026-02-19","amount":2200,"received":False},
                    {"id":"rakuten-1","type":"rakuten","name":"Rakuten","displayDate":"2026-02-14","isoDate":"2026-02-14","amount":4200,"received":False},
                    {"id":"rakuten-2","type":"rakuten","name":"Rakuten","displayDate":"2026-02-28","isoDate":"2026-02-28","amount":4200,"received":False}
                ]
            }
        ],
        "milestones": [
            {"id":"mile-1","amount":25000,"name":"iMac","reached":False},
            {"id":"mile-2","amount":50000,"name":"Foldable Smartphone","reached":False},
            {"id":"mile-3","amount":75000,"name":"DJI Device","reached":False},
            {"id":"mile-4","amount":100000,"name":"Motorbike","reached":False}
        ]
    }

def pay_collected(data):
    s = 0
    for mo in data["months"]:
        for pc in mo["paychecks"]:
            if pc["received"]:
                s += pc["amount"]
    return s

def pay_expected(data):
    t = 0
    for mo in data["months"]:
        for pc in mo["paychecks"]:
            t += pc["amount"]
    return t

def check_milestones():
    c = pay_collected(st.session_state["pay_data"])
    for m in st.session_state["pay_data"]["milestones"]:
        if not m["reached"] and c >= m["amount"]:
            m["reached"] = True
            st.balloons()
            st.snow()

def toggle_paycheck(month_id, paycheck_id, widget_key):
    new_val = st.session_state[widget_key]
    for mo in st.session_state["pay_data"]["months"]:
        if mo["id"] == month_id:
            for pc in mo["paychecks"]:
                if pc["id"] == paycheck_id:
                    pc["received"] = new_val
    check_milestones()

def next_pay():
    now = datetime.date.today()
    fut = []
    for mo in st.session_state["pay_data"]["months"]:
        for pc in mo["paychecks"]:
            if not pc["received"]:
                dt = datetime.datetime.strptime(pc["isoDate"], "%Y-%m-%d").date()
                if dt >= now:
                    fut.append((pc, dt))
    if not fut:
        return None
    fut.sort(key=lambda x: x[1])
    p, d = fut[0]
    days_left = (d - now).days
    if days_left < 5:
        color_class = "days-left-short"
    elif days_left < 10:
        color_class = "days-left-mid"
    else:
        color_class = "days-left-long"
    return {
        "name": p["name"],
        "amount": p["amount"],
        "daysLeft": days_left,
        "displayDate": p["displayDate"],
        "colorClass": color_class
    }

def month_status(m):
    if all(pc["received"] for pc in m["paychecks"]):
        return "Complete"
    now = datetime.datetime.now()
    mo_idx = {
        "January": 0,"February": 1,"March": 2,"April": 3,
        "May": 4,"June": 5,"July": 6,"August": 7,
        "September": 8,"October": 9,"November": 10,"December": 11
    }.get(m["name"], 0)
    if m["year"] > now.year or (m["year"] == now.year and mo_idx > now.month - 1):
        return "Future"
    if m["year"] == now.year and mo_idx == (now.month - 1):
        return "Current"
    return "Past"

def date_str(d):
    return d.strftime("%Y-%m-%d")

def find_kpi_for_date(hist, ds):
    for h in hist:
        if h["date"] == ds:
            return h
    return None

def compute_effort_score(kpis):
    s = 0
    if kpis["scotiaBank"]:
        s += 20
    if kpis["rakutenRewards"]:
        s += 20
    if kpis["workout"]:
        s += 20
    if kpis["onlineBusiness"]:
        s += 20
    s += min(kpis["approaches"], 3) * (10 / 3)
    if kpis["emailOutreach"]:
        s += 10
    return round(s)

def save_kpi(hist, ds, sc, kp):
    for i, h in enumerate(hist):
        if h["date"] == ds:
            hist[i] = {"date": ds, "score": sc, "kpis": kp}
            return hist
    hist.append({"date": ds, "score": sc, "kpis": kp})
    return hist

def change_date(days):
    nd = st.session_state["selected_date"] + datetime.timedelta(days=days)
    # Only allow going up to today's date
    if nd <= datetime.date.today():
        st.session_state["selected_date"] = nd
        existing = find_kpi_for_date(st.session_state["kpi_history"], date_str(nd))
        st.session_state["kpis"] = existing["kpis"] if existing else default_kpis()

def store_daily_kpi():
    ds = date_str(st.session_state["selected_date"])
    sc = compute_effort_score(st.session_state["kpis"])
    st.session_state["kpi_history"] = save_kpi(
        st.session_state["kpi_history"], ds, sc, st.session_state["kpis"]
    )

def get_week_data(hist):
    now = datetime.date.today()
    idx = now.weekday()
    monday = now - datetime.timedelta(days=idx)
    out = []
    for i in range(7):
        d = monday + datetime.timedelta(days=i)
        ds = date_str(d)
        e = find_kpi_for_date(hist, ds)
        out.append({
            "date": ds,
            "label": f"{d.month}/{d.day}",
            "score": e["score"] if e else None
        })
    return out

def get_month_data(hist):
    now = datetime.date.today()
    first = datetime.date(now.year, now.month, 1)
    count = (now - first).days + 1
    out = []
    for i in range(count):
        d = first + datetime.timedelta(days=i)
        ds = date_str(d)
        e = find_kpi_for_date(hist, ds)
        out.append({"date": ds, "label": str(d.day), "score": e["score"] if e else None})
    return out

def avg_score(ds):
    v = [x["score"] for x in ds if x["score"] is not None]
    return round(sum(v) / len(v)) if v else 0

st.set_page_config(page_title="Unified Dashboard", layout="wide")

def status_badge(sts):
    css_map = {
        "Complete": "status-complete",
        "Future": "status-future",
        "Current": "status-current",
        "Past": "status-past"
    }
    c = css_map.get(sts, "")
    return f"<span class='status-badge {c}'>{sts}</span>"

def extra_style_block():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');
        body {
          font-family: 'Poppins', sans-serif; font-size: 1.02rem;
          background: linear-gradient(to bottom right, #f3e7fe, #fde7f9);
        }
        .card {
          background-color: #fff; border-radius: 0.5rem; padding: 1rem;
          box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 1rem;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover { transform: scale(1.02); box-shadow: 0 8px 14px rgba(0,0,0,0.12); }
        .card-title { font-size: 0.9rem; color: #666; text-transform: uppercase; margin-bottom: 0.3rem; }
        .card-value { font-size: 1.3rem; font-weight: bold; color: #333; }
        .subtext { font-size: 0.8rem; color: #999; margin-top: 0.2rem; }
        .status-badge {
          display: inline-block; padding: 0.15rem 0.45rem; border-radius: 0.3rem;
          font-size: 0.75rem; margin-left: 0.5rem; background: #ddd; color: #444;
        }
        .status-complete { background: #c3f7c8; color: #226622; }
        .status-future { background: #cff3ff; color: #0077aa; }
        .status-current { background: #ffefc2; color: #aa7700; }
        .status-past { background: #f3f3f3; color: #777; }
        .stButton>button {
          background: linear-gradient(90deg, #4b8bbe, #6b68f1);
          color: white; border-radius: 0.4rem; border: none; font-size: 0.8rem;
          padding: 0.5rem 1rem; cursor: pointer; transition: background 0.3s ease;
        }
        .stButton>button:hover { background: linear-gradient(90deg, #3b7aa2, #5145ec); }
        .daily-checks-label {
          font-size: 1rem; font-weight: 500; margin-bottom: 0.5rem; color: #444;
        }
        .approach-counter {
          text-align: center; font-size: 1.2rem; font-weight: bold;
        }
        [role='progressbar'] > div > div { transition: width 0.7s ease; }
        .approaches-max {
          background-color: rgba(255, 100, 100, 0.1);
          border: 1px solid #ff6464; border-radius: 0.3rem; padding: 0.3rem;
        }
        .gradient-text {
          background: linear-gradient(to right, #ff512f, #dd2476);
          -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .days-left-short { color: #e74c3c; font-weight: 700; }
        .days-left-mid { color: #f39c12; font-weight: 600; }
        .days-left-long { color: #27ae60; font-weight: 500; }
        .stCheckbox>div {
          border: 1px solid rgba(0,0,0,0.05);
          border-radius: 0.3rem; padding: 0.3rem 0.6rem; margin-bottom: 0.3rem;
        }
        .date-nav {
          display: flex; justify-content: center; align-items: center;
          gap: 1rem; margin-bottom: 1rem;
        }
        .approach-bar {
          display: flex; align-items: center; gap: 0.7rem;
          margin-bottom: 1rem; margin-top: 0.5rem;
        }
        .checks-and-approaches {
          display: flex; gap: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def double_code_appearance():
    extra_style_block()
    extra_style_block()

def reset_daily_kpis():
    st.session_state["kpis"] = default_kpis()

def main():
    init_states()
    check_milestones()
    st.title("🍎 Performance & Pay Dashboard")

    # Top KPI cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        collected = pay_collected(st.session_state["pay_data"])
        expected_val = pay_expected(st.session_state["pay_data"])
        pct = 0 if expected_val == 0 else int((collected / expected_val) * 100)
        st.markdown("<div class='card' style='background:#e8f2ff;'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Pay Progress</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-value'>{pct}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='subtext'>${collected:,} / ${expected_val:,}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        nxt = next_pay()
        st.markdown("<div class='card' style='background:#fce8ff;'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Next Paycheck</div>", unsafe_allow_html=True)
        if nxt:
            st.markdown(f"<div class='card-value'>${nxt['amount']:,}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='subtext'>{nxt['name']} in "
                f"<span class='{nxt['colorClass']}'>{nxt['daysLeft']} days</span></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div class='card-value'>All Received</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        daily = compute_effort_score(st.session_state["kpis"])
        st.markdown("<div class='card' style='background:#fffae6;'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Today's Effort</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-value gradient-text'>{daily}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='subtext'>{st.session_state['selected_date']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        wd = get_week_data(st.session_state["kpi_history"])
        wave = avg_score(wd)
        st.markdown("<div class='card' style='background:#ecffe8;'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>7-Day Avg</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-value'>{wave}%</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtext'>Weekly Score</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Daily KPI", "KPI Analysis", "Finances"])

    with tab1:
        st.subheader("Daily KPI Logging")

        # Date controls in one row
        st.write("<div class='date-nav'>", unsafe_allow_html=True)
        if st.button("◀️ Previous Day"):
            change_date(-1)
        st.markdown(
            f"<span style='font-weight:bold;'>{st.session_state['selected_date'].strftime('%A, %B %d, %Y')}</span>",
            unsafe_allow_html=True
        )
        if st.button("Next Day ▶️"):
            change_date(1)
        st.write("</div>", unsafe_allow_html=True)

        # Row with checkboxes & approaches
        st.write("<div class='checks-and-approaches'>", unsafe_allow_html=True)

        # Left: today's checks
        st.write("<div>", unsafe_allow_html=True)
        st.markdown("<div class='daily-checks-label'>Today's Checks</div>", unsafe_allow_html=True)
        st.session_state["kpis"]["scotiaBank"] = st.checkbox("Scotia Bank", value=st.session_state["kpis"]["scotiaBank"])
        st.session_state["kpis"]["rakutenRewards"] = st.checkbox("Rakuten Rewards", value=st.session_state["kpis"]["rakutenRewards"])
        st.session_state["kpis"]["workout"] = st.checkbox("Workout", value=st.session_state["kpis"]["workout"])
        st.session_state["kpis"]["onlineBusiness"] = st.checkbox("Online Business", value=st.session_state["kpis"]["onlineBusiness"])
        st.session_state["kpis"]["emailOutreach"] = st.checkbox("Email Outreach", value=st.session_state["kpis"]["emailOutreach"])
        st.write("</div>", unsafe_allow_html=True)

        # Right: approaches
        st.write("<div>", unsafe_allow_html=True)
        st.markdown("<div class='daily-checks-label'>Approaches</div>", unsafe_allow_html=True)
        st.write("<div class='approach-bar'>", unsafe_allow_html=True)
        minus_clicked = st.button("–", key="minus_approach")
        box_class = "approaches-max" if st.session_state["kpis"]["approaches"] == 3 else ""
        st.markdown(
            f"<div class='approach-counter {box_class}'>{st.session_state['kpis']['approaches']}</div>",
            unsafe_allow_html=True
        )
        plus_clicked = st.button("➕", key="plus_approach")
        st.write("</div>", unsafe_allow_html=True)

        if minus_clicked:
            st.session_state["kpis"]["approaches"] = max(0, st.session_state["kpis"]["approaches"] - 1)
        if plus_clicked and st.session_state["kpis"]["approaches"] < 3:
            st.session_state["kpis"]["approaches"] += 1
        st.write("</div>", unsafe_allow_html=True)

        st.write("</div>", unsafe_allow_html=True)  # end .checks-and-approaches

        # Save/Reset buttons
        col_s, col_r = st.columns([1,1])
        with col_s:
            if st.button("Save Daily KPI"):
                store_daily_kpi()
                st.success("Today's KPI saved.")
        with col_r:
            if st.button("Reset Daily KPI"):
                reset_daily_kpis()

    with tab2:
        st.subheader("Weekly & Monthly KPI Analysis")
        w_data = pd.DataFrame(get_week_data(st.session_state["kpi_history"]))
        st.markdown("**Weekly Trend**")
        if not w_data.empty:
            wchart = alt.Chart(w_data).mark_area(line=True, point=True).encode(
                x=alt.X("label", title="Day", sort=None),
                y=alt.Y("score", scale=alt.Scale(domain=[0, 100]), title="Score"),
                tooltip=["date", "score"]
            ).properties(height=250)
            st.altair_chart(wchart, use_container_width=True)
        else:
            st.info("No weekly KPI data yet.")

        st.markdown("**Monthly Trend**")
        m_data = pd.DataFrame(get_month_data(st.session_state["kpi_history"]))
        if not m_data.empty:
            mchart = alt.Chart(m_data).mark_area(line=True, point=True).encode(
                x=alt.X("label", title="Day of Month", sort=None),
                y=alt.Y("score", scale=alt.Scale(domain=[0, 100]), title="Score"),
                tooltip=["date", "score"]
            ).properties(height=250)
            st.altair_chart(mchart, use_container_width=True)
        else:
            st.info("No monthly KPI data yet.")

        st.write("**All KPI Records**")
        df_kpi = pd.DataFrame(st.session_state["kpi_history"])
        if not df_kpi.empty:
            st.dataframe(df_kpi.style.format({"score": "{:.0f}"}), use_container_width=True)
        else:
            st.write("No records yet.")

    with tab3:
        st.subheader("Financial Progress")
        cval = pay_collected(st.session_state["pay_data"])
        eval_ = pay_expected(st.session_state["pay_data"])
        ratio = 0 if eval_ == 0 else int((cval / eval_) * 100)
        st.metric("Collected vs Expected", f"{ratio}%", f"${cval:,} / ${eval_:,}")
        st.progress(ratio / 100)

        st.write("### Milestones")
        for ml in st.session_state["pay_data"]["milestones"]:
            icon = "✅" if ml["reached"] else "🔒"
            st.write(f"{icon} ${ml['amount']:,} - {ml['name']}")

        npay = next_pay()
        st.write("### Next Paycheck")
        if npay:
            st.info(
                f"{npay['name']} on {npay['displayDate']} for ${npay['amount']:,}, in "
                f"{npay['daysLeft']} days"
            )
        else:
            st.write("No upcoming checks.")
        st.write("---")

        st.write("### Monthly Paychecks")
        by_year = {}
        for mo in st.session_state["pay_data"]["months"]:
            by_year.setdefault(mo["year"], []).append(mo)
        for yr in sorted(by_year.keys()):
            st.write(f"#### {yr}")
            for mobj in by_year[yr]:
                st.write(
                    f"**{mobj['name']} {mobj['year']}** {status_badge(month_status(mobj))}",
                    unsafe_allow_html=True
                )
                mon_c = sum(pc["amount"] for pc in mobj["paychecks"] if pc["received"])
                mon_e = sum(pc["amount"] for pc in mobj["paychecks"])
                st.write(f"Collected: ${mon_c:,} / ${mon_e:,}")
                for pc in mobj["paychecks"]:
                    key_id = f"{mobj['id']}-{pc['id']}"
                    st.checkbox(
                        f"{pc['displayDate']} - ${pc['amount']:,} ({pc['name']})",
                        value=pc["received"],
                        key=key_id,
                        on_change=toggle_paycheck,
                        args=(mobj["id"], pc["id"], key_id),
                    )
        st.write("---")
        st.write("### Monthly Collected Chart")
        rows = []
        for mo in st.session_state["pay_data"]["months"]:
            label = f"{mo['name']} {mo['year']}"
            val = sum(p["amount"] for p in mo["paychecks"] if p["received"])
            rows.append({"Month": label, "Collected": val})
        df_pay = pd.DataFrame(rows)
        if not df_pay.empty:
            chart = alt.Chart(df_pay).mark_bar().encode(
                x=alt.X("Month:N", sort=None),
                y=alt.Y("Collected:Q", title="Collected"),
                tooltip=["Month", "Collected"]
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("No paychecks received yet.")

if __name__ == "__main__":
    double_code_appearance()
    main()
    double_code_appearance()