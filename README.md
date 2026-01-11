# Excel Data Chatbot with OpenAI 📊

A bilingual (Arabic/English) Streamlit chatbot application that uses OpenAI's GPT-4 to intelligently query Excel data and generate insights with visualizations.

## Features ✨

- 🤖 **AI-Powered Querying**: Uses OpenAI GPT-4 to understand natural language questions about your data
- 🌐 **Bilingual Support**: Automatically detects and responds in Arabic or English
- 📊 **Auto-Visualization**: Generates relevant charts and graphs based on your queries
- 🔍 **Smart Column Mapping**: Understands both Arabic and English column names
- 💬 **Chat Interface**: Interactive conversation-style interface with history
- 📈 **Real-time Analysis**: Get summaries, statistics, and insights instantly
- 🗂️ **Database Ready**: Built with extensibility to support database connections in the future

## Data Structure 📋

The application is designed to work with property/land data containing:

- **45,179 records** with 15 columns
- Property information (parcels, plots, regions, villages)
- Area measurements and property use classifications
- Connection details and dates
- **Bilingual content**: Mix of Arabic and English data

### Columns with Arabic Content ⚠️

The following columns contain Arabic values:
- `REGN` (Region / المنطقة)
- `WLYA` (Wilayat / الولاية)
- `VILG` (Village / القرية)
- `PUSE` (Property Use / الاستخدام)
- `SUB_PUSE_DESC` (Sub Property Use)
- `ZONE_NO` (Zone Number)
- `المنطقة` (Area)
- `نوع التوصيل` (Connection Type)

**Important**: When querying in Arabic, the system will search for Arabic values in these columns.

## Installation 🚀

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Step 1: Clone or Download

Download the application files to your local machine.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up OpenAI API Key

You have two options:

**Option 1: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

On Windows:
```cmd
set OPENAI_API_KEY=your-api-key-here
```

**Option 2: Enter in App**
You can enter the API key directly in the sidebar when running the app.

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Usage 💡

### Example Queries in English

1. **General Statistics**
   - "How many total records are in the dataset?"
   - "What is the average parcel area?"
   - "Show me the distribution by region"

2. **Specific Filtering**
   - "How many properties are in Muscat region?"
   - "What's the total area of residential properties?"
   - "Show properties larger than 1000 m²"

3. **Temporal Analysis**
   - "How many properties were registered in 2024?"
   - "Show the trend of registrations over time"
   - "What's the distribution by year?"

4. **Comparisons**
   - "Compare the number of properties across different regions"
   - "What's the difference between residential and social housing counts?"

### Example Queries in Arabic / أمثلة على الاستعلامات بالعربية

1. **إحصائيات عامة**
   - "كم عدد السجلات الإجمالي في البيانات؟"
   - "ما متوسط مساحة القطع؟"
   - "أظهر التوزيع حسب المنطقة"

2. **استعلامات محددة**
   - "كم عدد العقارات في محافظة مسقط؟"
   - "ما إجمالي مساحة العقارات السكنية؟"
   - "أظهر العقارات التي مساحتها أكبر من 1000 متر مربع"

3. **تحليل زمني**
   - "كم عدد العقارات المسجلة في 2024؟"
   - "أظهر اتجاه التسجيلات عبر الزمن"
   - "ما التوزيع حسب السنة؟"

4. **مقارنات**
   - "قارن عدد العقارات في المناطق المختلفة"
   - "ما الفرق بين عدد المساكن السكنية والمساكن الاجتماعية؟"

### Query Tips 💭

1. **Be Specific**: The more specific your question, the better the answer
2. **Use Natural Language**: Ask questions as you would to a human analyst
3. **Arabic Values**: When querying Arabic columns, use the exact Arabic terms (e.g., "سكني" not "residential")
4. **Request Visualizations**: Ask for charts, graphs, or distributions for visual insights
5. **Follow-up Questions**: You can ask follow-up questions based on previous responses

## Architecture 🏗️

### Components

1. **Streamlit Interface**: Web-based chat UI with sidebar configuration
2. **LangChain Agent**: Pandas DataFrame agent for intelligent data querying
3. **OpenAI GPT-4**: LLM for understanding queries and generating responses
4. **Plotly**: Interactive visualization library for charts and graphs

### How It Works

```
User Query → LangChain Agent → Pandas Operations → Response Generation
                ↓                      ↓                    ↓
           OpenAI GPT-4          DataFrame API        Visualization
```

1. User submits a query in Arabic or English
2. LangChain agent uses OpenAI to understand the intent
3. Agent generates appropriate pandas operations
4. Results are formatted and returned to user
5. Relevant visualizations are automatically generated

## Future Enhancements 🚀

- [ ] Database connectivity (PostgreSQL, MySQL, etc.)
- [ ] Export results to Excel/CSV
- [ ] Advanced filtering interface
- [ ] Custom visualization builder
- [ ] Query templates
- [ ] Multi-file support
- [ ] Data validation and cleaning tools

## Column Reference 📚

| Column | English Name | Arabic Name | Description |
|--------|--------------|-------------|-------------|
| PAR_PIN | Parcel ID | معرف القطعة | Unique parcel identifier |
| PLT1_NO | Plot Number | رقم المخطط | Plot number |
| REGN | Region | المنطقة | Region name (Arabic) |
| WLYA | Wilayat | الولاية | Wilayat name (Arabic) |
| VILG | Village | القرية | Village name (Arabic) |
| PUSE | Property Use | الاستخدام | Property use type (Arabic) |
| SUB_PUSE_DESC | Sub Use | وصف الاستخدام الفرعي | Sub property use (Arabic) |
| PAR_AREA | Parcel Area | مساحة القطعة | Area in square meters |
| ZONE_NO | Zone Number | رقم المنطقة | Zone identifier |
| DOC_DATE | Document Date | تاريخ الوثيقة | Registration date |
| YR | Year | السنة | Year (2023, 2024, 2025) |
| رقم العداد | Meter Number | رقم العداد | Meter/Account number |
| المنطقة | Area | المنطقة | Area (bilingual format) |
| تاريخ التوصيل | Connection Date | تاريخ التوصيل | Connection date |
| نوع التوصيل | Connection Type | نوع التوصيل | Permanent/Temporary |

## Troubleshooting 🔧

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is valid
   - Check that it's properly set in environment variable or entered in the app

2. **Import Errors**
   - Run `pip install -r requirements.txt` to install all dependencies
   - Ensure you're using Python 3.8+

3. **Arabic Text Display**
   - Make sure your browser supports Arabic font rendering
   - Some terminals may not display Arabic correctly

4. **Slow Responses**
   - Complex queries may take 5-30 seconds
   - OpenAI API rate limits may affect response time

5. **Incorrect Results for Arabic Queries**
   - Verify you're using exact Arabic values from the dataset
   - Check the column reference for correct Arabic terms

## License 📄

This application is provided as-is for data analysis purposes.

## Support 💬

For issues or questions:
1. Check the example queries above
2. Review the column reference
3. Ensure your API key is valid and has sufficient credits

## Credits 🙏

Built with:
- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.com/)
- [OpenAI](https://openai.com/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)
