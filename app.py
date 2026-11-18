
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from algorithms import fifo, lru, optimal

st.set_page_config(
    page_title="MemorySim",
    page_icon="💻",
    layout="wide"
)

st.title("💻 MemorySim")
st.subheader("Virtual Memory & Page Replacement Simulator")

st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
div[data-testid="stMetric"] {
    background: #1e293b;
    padding: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ Settings")

page_input = st.sidebar.text_input(
    "Page Reference String",
    "1,2,3,1,4,5,2,1,2,3"
)

frames = st.sidebar.number_input(
    "Number of Frames",
    min_value=1,
    max_value=10,
    value=3
)

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["FIFO", "LRU", "Optimal"]
)

if st.sidebar.button("🚀 Run Simulation"):
    try:
        pages = [int(x.strip()) for x in page_input.split(",")]

        if not page_input.strip() or any(x < 0 for x in pages):
            st.error("Enter valid non-negative page numbers.")
            st.stop()

        if algorithm == "FIFO":
            result = fifo(pages, int(frames))
        elif algorithm == "LRU":
            result = lru(pages, int(frames))
        else:
            result = optimal(pages, int(frames))

        st.session_state["result"] = (
            result, pages, algorithm, int(frames)
        )

    except ValueError:
        st.error("Please enter valid numbers separated by commas.")

if "result" in st.session_state:

    result, pages, selected, frame_count = st.session_state["result"]
    history, hits, faults = result

    st.divider()
    st.header("📊 Simulation Dashboard")

    total = len(pages)
    hit_ratio = hits / total * 100

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Pages", total)
    c2.metric("Page Hits", hits)
    c3.metric("Page Faults", faults)
    c4.metric("Hit Ratio", f"{hit_ratio:.2f}%")

    st.subheader("🧠 Memory Frame Visualization")

    table = {"Page": [], "Status": []}

    for i in range(frame_count):
        table[f"Frame {i+1}"] = []

    for item in history:
        table["Page"].append(item["Page"])
        table["Status"].append(item["Status"])

        for i in range(frame_count):
            value = (
                item["Frames"][i]
                if i < len(item["Frames"])
                else "-"
            )
            table[f"Frame {i+1}"].append(value)

    df = pd.DataFrame(table)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("📈 Performance Analysis")

    fig, ax = plt.subplots()
    ax.bar(["Page Hits", "Page Faults"], [hits, faults])
    ax.set_ylabel("Count")
    ax.set_title(f"{selected} Performance")
    st.pyplot(fig)
    plt.close(fig)

    st.success("Simulation completed successfully!")

    st.divider()
    st.header("⚖️ Compare All Algorithms")

    if st.button("Compare FIFO, LRU & Optimal"):

        f = fifo(pages, frame_count)
        l = lru(pages, frame_count)
        o = optimal(pages, frame_count)

        comparison = pd.DataFrame({
            "Algorithm": ["FIFO", "LRU", "Optimal"],
            "Page Hits": [f[1], l[1], o[1]],
            "Page Faults": [f[2], l[2], o[2]]
        })

        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True
        )

        fig, ax = plt.subplots()
        ax.bar(
            comparison["Algorithm"],
            comparison["Page Faults"]
        )
        ax.set_title("Algorithm Comparison")
        ax.set_ylabel("Page Faults")
        st.pyplot(fig)
        plt.close(fig)

        best = comparison.loc[
            comparison["Page Faults"].idxmin(),
            "Algorithm"
        ]

        st.success(f"{best} has the lowest page faults!")

else:
    st.info("Enter your settings and click Run Simulation.")

st.divider()
st.caption("MemorySim | Virtual Memory & Page Replacement Simulator")

