import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
# from numerize import numerize
import warnings 
warnings.filterwarnings('ignore')


st.set_page_config(layout='centered')

# read csv
df = pd.read_csv('dataset_baruu.csv')
print(df.head())

# df['order_date'] = pd.to_datetime(df['order_date'])
# df['ship_date'] = pd.to_datetime(df['ship_date'])

# df['order_year'] = df['order_date'].dt.year

# CURR_YEAR = max(df['order_date'].dt.year)
# PREV_YEAR = CURR_YEAR - 1

st.title("Stunting Kabupaten Jayapura Tahun 2021/2022")

# paramemter start ke 1
# Fungsi untuk membuat diagram batang
def create_bar_chart(kecamatan, stunting):
    fig, ax = plt.subplots(figsize=(10, 6))  # Membuat objek gambar dan sumbu
    ax.bar(kecamatan, stunting)  # Melakukan plotting di sumbu
    ax.set_xlabel('Kecamatan')  # Mengatur label sumbu x
    ax.set_ylabel('Stunting')   # Mengatur label sumbu y
    ax.set_title('Diagram Batang Stunting per Kecamatan')  # Memberi judul plot
    plt.xticks(rotation=90)  # Memutar label kecamatan agar tegak
    st.pyplot(fig)  # Menampilkan plot menggunakan st.pyplot()

# Daftar kecamatan dan data stunting (contoh)
kecamatan = ["Sentani", "Sentani Timur", "Depapre", "Sentani Barat", "Kemtuk", "Kemtuk Gresi", "Nimboran", "Nimbokrang", "Unurum Guay", "Demta","Kaureh" "Ebungfao", "Waibu", "Namblong", "Yapsi", "Airu", "Raveni Rara", "Yokari"]
stunting = [10, 20, 15, 25, 30, 35, 20, 15, 10, 5, 10, 20, 15, 10, 20, 25, 15]
resiko_stunting = ["Beresiko Stunting","Tidak Beresiko stunting"]

# Menampilkan judul dan deskripsi
st.header('Aplikasi Diagram Batang Stunting per Kecamatan')
st.write('Aplikasi ini menampilkan diagram batang yang menunjukkan tingkat stunting di setiap kecamatan.')

# Menambahkan parameter menggunakan sidebar
with st.sidebar:
    st.title('Parameter')
    # Tambahkan slider untuk mengatur tingkat stunting
    stunting_threshold = st.slider('Batas Stunting', min_value=0, max_value=50, value=20, step=5)

# Filter kecamatan berdasarkan batas stunting
filtered_kecamatan = [kecamatan[i] for i in range(len(kecamatan)) if stunting[i] > stunting_threshold]
filtered_stunting = [stunting[i] for i in range(len(kecamatan)) if stunting[i] > stunting_threshold]

# Memanggil fungsi untuk membuat diagram batang
create_bar_chart(filtered_kecamatan, filtered_stunting)
# parameter end

# parameter start

# Menampilkan data storytelling berdasarkan kecamatan
st.write("## Data Storytelling Berdasarkan Kecamatan")

# Narasi untuk setiap kecamatan
for kecamatan, stunting_rate in zip(filtered_kecamatan, filtered_stunting):
    st.write(f"### Kecamatan {kecamatan}")
    st.write(f"Tingkat stunting di Kecamatan {kecamatan} adalah {stunting_rate}%.")

    # Menambahkan narasi spesifik berdasarkan tingkat stunting
    if stunting_rate > 20:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} tergolong tinggi. Hal ini memerlukan perhatian khusus dari pemerintah setempat untuk mengimplementasikan program-program kesehatan yang lebih efektif.")
    elif stunting_rate > 10:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} tergolong sedang. Upaya-upaya pencegahan dan intervensi harus terus dilakukan untuk mencegah peningkatan lebih lanjut.")
    else:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} relatif rendah. Ini menunjukkan keberhasilan dari kebijakan atau program kesehatan yang telah diterapkan di wilayah ini.")

    # Menambahkan visualisasi diagram batang untuk mendukung narasi
    st.write(f"#### Diagram Batang Tingkat Stunting di Kecamatan {kecamatan}")
    create_bar_chart([kecamatan], [stunting_rate])

# parameter end

# parameter end data storytelling

# # 1 periksa tahun terakhir dari data
# # itung total sales, banyaknya order, banyaknya kosumen, profit %
# # di tahun tersebut

# parameter yang lain start


# parameter lain ending


# data = pd.pivot_table(
#     data=df,
#     index='order_year',
#     aggfunc={
#         'sales':'sum',
#         'profit':'sum',
#         'order_id':pd.Series.nunique,
#         'customer_id':pd.Series.nunique
#     }
# ).reset_index()

# data['gpm'] = 100.0 * data['profit'] / data['sales']

# mx_sales, mx_order, mx_customer, mx_gpm = st.columns(4)

# with mx_sales:

#     curr_sales = data.loc[data['order_year']==CURR_YEAR, 'sales'].values[0]
#     prev_sales = data.loc[data['order_year']==PREV_YEAR, 'sales'].values[0]
    
#     sales_diff_pct = 100.0 * (curr_sales - prev_sales) / prev_sales

#     # st.metric("Sales", value=numerize.numerize(curr_sales), delta=f'{sales_diff_pct:.2f}%')

# with mx_order:
#     st.metric("Number of Order", value=100, delta=10)


# freq = st.selectbox("Freq", ['Harian','Bulanan'])

# timeUnit = {
#     'Harian':'yearmonthdate',
#     'Bulanan':'yearmonth'
# }

# st.header("Sales trend")
# # altair membuat object berupa chart dengan data di dalam parameter
# sales_line = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_line().encode(
#     alt.X('order_date', title='Order Date', timeUnit=timeUnit[freq]),
#     alt.Y('sales', title='Revenue', aggregate='sum')
# )

# st.altair_chart(sales_line,use_container_width=True)

# sales_bar = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_bar().encode(
#     alt.X('order_date', title='Order Date', timeUnit=timeUnit[freq]),
#     alt.Y('sales', title='Revenue', aggregate='sum')
# )

# # Bikin 4 kolom berisi sales dari tiap kategori
# # Setiap kolom mewakili region yang berbeda

# st.altair_chart(sales_bar,use_container_width=True)

# st.dataframe(df)

# st.dataframe(data, use_container_width=True)


# start startangle ke-2

# Data dummy untuk kepala keluarga
data_keluarga = {
    "nelayan": {"beresiko": 77, "tidak_beresiko": 480},
    "pedagang": {"beresiko": 57, "tidak_beresiko": 420}
}

# Aplikasi Streamlit
st.title('Populasi Kepala Keluarga Berdasarkan Profesi dan Resiko Stunting')

# Dropdown untuk memilih profesi
profesi_options = ['nelayan', 'pedagang']
selected_profesi = st.selectbox('Pilih Profesi:', profesi_options)

# Mendapatkan data berdasarkan profesi yang dipilih
data = data_keluarga.get(selected_profesi)

if data is not None:
    # Dropdown untuk memilih resiko stunting
    resiko_options = list(data.keys())
    selected_resiko = st.selectbox('Pilih Resiko Stunting:', resiko_options)

    # Mendapatkan jumlah kepala keluarga berdasarkan resiko stunting yang dipilih
    jumlah = data.get(selected_resiko)

    # Mengambil labels dan values dari data
    labels = list(data.keys())
    values = list(data.values())

    # Membuat pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Populasi Kepala Keluarga\nBerdasarkan Profesi dan Resiko Stunting')

    # Menampilkan pie chart
    st.pyplot(fig)
else:
    st.write("Data tidak ditemukan untuk profesi yang dipilih.")

# end startangle
# end method grid

# start storytelling ke 2
# Data storytelling
st.header('Data Storytelling')

# Narasi
st.write("Dalam analisis ini, kita melihat distribusi populasi kepala keluarga berdasarkan profesi dan tingkat resiko stunting. Profesi yang dianalisis adalah nelayan dan pedagang.")

# Narasi berdasarkan profesi yang dipilih
if selected_profesi:
    st.write(f"Kita fokus pada populasi kepala keluarga dengan profesi {selected_profesi}.")
    if selected_profesi == 'nelayan':
        st.write("Nelayan adalah profesi yang memiliki resiko stunting tertinggi, dengan 77% kepala keluarga dalam kategori beresiko.")
    elif selected_profesi == 'pedagang':
        st.write("Pedagang memiliki resiko stunting yang sedikit lebih rendah dibandingkan nelayan, dengan 57% kepala keluarga dalam kategori beresiko.")

# Narasi berdasarkan tingkat resiko stunting yang dipilih
if selected_resiko:
    st.write(f"Kita juga dapat melihat distribusi populasi berdasarkan tingkat resiko stunting. Jika kita memilih resiko stunting {selected_resiko}, maka sebanyak {jumlah} kepala keluarga dalam kategori tersebut.")

# Kesimpulan
st.write("Dari analisis ini, kita dapat menyimpulkan bahwa nelayan memiliki resiko stunting yang lebih tinggi dibandingkan dengan pedagang. Hal ini menunjukkan perlunya perhatian khusus terhadap kesehatan dan nutrisi di kalangan nelayan.")

# end  storytelling ke 3

