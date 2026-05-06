@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    print("🚀 UPLOAD ENDPOINT HIT")

    try:
        print("📄 FILE RECEIVED:", file.filename)

        contents = await file.read()

        print("📦 FILE SIZE:", len(contents))

        with open("temp.pdf", "wb") as f:
            f.write(contents)

        import pdfplumber

        text = ""

        with pdfplumber.open("temp.pdf") as pdf:
            print("📄 PDF OPENED, pages:", len(pdf.pages))

            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                print(f"📄 PAGE {i} TEXT LENGTH:", len(page_text) if page_text else 0)

                if page_text:
                    text += page_text + "\n"

        print("🧠 EXTRACTED TEXT SAMPLE:", text[:300])

        import re
        matches = re.findall(r"\b([A-Z]{1,5})\b.*?(\d+\.?\d*)", text)

        print("🔍 MATCHES FOUND:", matches[:10])

        portfolio = {}

        for symbol, qty in matches:
            try:
                portfolio[symbol] = float(qty)
            except:
                pass

        print("📊 FINAL PORTFOLIO:", portfolio)

        import json
        with open("portfolio.json", "w") as f:
            json.dump(portfolio, f)

        return {"status": "success", "portfolio": portfolio}

    except Exception as e:
        print("❌ ERROR IN UPLOAD:", str(e))
        return {"status": "error", "message": str(e)}
        with open("portfolio.json", "w") as f:
            json.dump(portfolio, f)

        return {
            "status": "success",
            "portfolio": portfolio
        }

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return {"status": "error", "message": str(e)}
        json.dump(portfolio, f)

    return {
        "status": "PDF processed",
        "portfolio": portfolio
    }
