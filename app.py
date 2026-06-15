import streamlit as st

st.title("重複組合せタッチパネル")

fruits = ["りんご", "なし", "みかん"]
target = 5

if "counts" not in st.session_state:
    st.session_state.counts = {f: 0 for f in fruits}

st.write("果物を合計5個になるように選びましょう。")

cols = st.columns(3)

for i, fruit in enumerate(fruits):
    with cols[i]:
        st.subheader(fruit)
        st.write("🍎" * st.session_state.counts[fruit] if fruit == "りんご" else
                 "🍐" * st.session_state.counts[fruit] if fruit == "なし" else
                 "🍊" * st.session_state.counts[fruit])

        c1, c2 = st.columns(2)

        with c1:
            if st.button("＋", key=f"plus_{fruit}"):
                if sum(st.session_state.counts.values()) < target:
                    st.session_state.counts[fruit] += 1

        with c2:
            if st.button("−", key=f"minus_{fruit}"):
                if st.session_state.counts[fruit] > 0:
                    st.session_state.counts[fruit] -= 1

total = sum(st.session_state.counts.values())

st.divider()
st.write(f"現在の合計：{total} / {target}")

if total == target:
    st.success("5個そろいました。")
    st.write(st.session_state.counts)
elif total < target:
    st.info(f"あと {target - total} 個選べます。")
else:
    st.error("選びすぎです。")

if st.button("リセット"):
    st.session_state.counts = {f: 0 for f in fruits}
    st.rerun()
    