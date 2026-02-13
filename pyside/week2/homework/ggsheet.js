function onOpen() {

    var ui = SpreadsheetApp.getUi();

    ui.createMenu('อัปเดตข้อมูล Statement')

        .addItem('กดเพื่อเริ่มอัปเดต', 'mergeFinancialStatements')

        .addToUi();

}



function mergeFinancialStatements() {

    const ss = SpreadsheetApp.getActiveSpreadsheet();

    let destSheet = ss.getSheetByName("Summary");

    if (!destSheet) destSheet = ss.insertSheet("Summary");



    // ID ของไฟล์แหล่งข้อมูลต่างๆ

    const IT_NIGHT_ID = "1Sv2Xr4CEFgLzFgMCXL7_QV3hGhDiS4rZWLq3-H-MYK4";

    const LOG_LTS_ID = "1g3PqquXCpPSv6ujv8-pjGDUUz9d5RroDrv1hEDKgwRY";

    const NAME_LIST_ID = "1QwLpYucj21qh2b7rjJ0yDNHedxxMzfausdzaFbBT0NM";

    const OTHER_INCOME_ID = "1iKLu3jZ3933wzk7PY-YIshrB2_qHqL5L2Gza8bbDTjg";

    const COLOR_SPORTS_ID = "1QpGTfDozrwG65bNyNeLiuSrQx1KQnh7cQXHIdAwXYuA";



    let allData = [];



    // 1. จัดการรายชื่อและย่อนามสกุล

    let nameMap = {};

    try {

        const nameSheet = SpreadsheetApp.openById(NAME_LIST_ID).getSheetByName("all");

        const nameValues = nameSheet.getRange(2, 1, nameSheet.getLastRow() - 1, 3).getValues();

        const leadingVowels = ['เ', 'แ', 'โ', 'ไ', 'ใ'];



        nameValues.forEach(row => {

            let prefix = (row[1] || "").trim();

            let fullNameRaw = (row[2] || "").trim();

            let parts = fullNameRaw.split(/\s+/);

            let firstName = parts[0];

            let lastName = parts.length > 1 ? parts[1] : "";

            let formattedName = prefix + firstName;



            if (lastName !== "") {

                let firstChar = lastName.charAt(0);

                if (leadingVowels.indexOf(firstChar) > -1 && lastName.length > 1) firstChar = lastName.charAt(1);

                formattedName += " " + firstChar + ".";

            }

            nameMap[row[0].toString()] = formattedName;

        });

    } catch (e) { console.log("NameList Error: " + e.message); }



    // 2. ดึงข้อมูล IT NIGHT

    try {

        const itSheet = SpreadsheetApp.openById(IT_NIGHT_ID).getSheetByName("activity_statement");

        const itValues = itSheet.getRange(2, 1, itSheet.getLastRow() - 1, 9).getValues();

        itValues.forEach(row => {

            if (row[0]) {

                let dateObj = new Date(row[0]);

                let timeStr = Utilities.formatDate(dateObj, "GMT+7", "HH:mm");

                allData.push([dateObj, timeStr, row[1], Number(row[4]) || 0, Number(row[3]) || 0, 0, row[2], row[7]]);

            }

        });

    } catch (e) { }



    // 3. ดึงข้อมูล LOG_LTS

    try {

        const logSheet = SpreadsheetApp.openById(LOG_LTS_ID).getSheetByName("MANUAL");

        const logValues = logSheet.getRange(2, 1, logSheet.getLastRow() - 1, 8).getValues();

        logValues.forEach(row => {

            if (row[0]) {

                let dateObj = new Date(row[0]);

                let timeStr = Utilities.formatDate(dateObj, "GMT+7", "HH:mm");

                let studentName = nameMap[row[1].toString()] || row[1].toString();

                allData.push([dateObj, timeStr, "รับเงินสาขา", 0, 40, 0, row[7], `โอนจาก ${studentName} (${row[5]})`]);

            }

        });

    } catch (e) { }



    // 4. ดึงข้อมูลจากไฟล์ "เก็บเงินกีฬาสี68"

    try {

        const sportSheet = SpreadsheetApp.openById(COLOR_SPORTS_ID).getSheetByName("Form Responses 1");

        const sportValues = sportSheet.getRange(2, 1, sportSheet.getLastRow() - 1, 2).getValues();

        sportValues.forEach(row => {

            if (row[0]) {

                let dateObj = new Date(row[0]);

                let timeStr = Utilities.formatDate(dateObj, "GMT+7", "HH:mm");

                let studentId = row[1].toString();

                let studentName = nameMap[studentId] || studentId;

                allData.push([dateObj, timeStr, "รับเงินกีฬาสี", 0, 70, 0, "JAMPA68", `โอนจาก ${studentName}`]);

            }

        });

    } catch (e) { console.log("ColorSports Error: " + e.message); }



    // 5. ดึงข้อมูล OTH & SPN

    const fetchExtra = (sheetName, typeCode) => {

        try {

            const extraSheet = SpreadsheetApp.openById(OTHER_INCOME_ID).getSheetByName(sheetName);

            const extraValues = extraSheet.getRange(2, 1, extraSheet.getLastRow() - 1, 5).getValues();

            extraValues.forEach(row => {

                if (row[0]) {

                    let dateObj = new Date(row[0]);

                    let amount = Number(row[2].toString().replace(/[฿,]/g, '')) || 0;

                    allData.push([dateObj, "0:00", typeCode, 0, amount, 0, "OTH", row[1] + (row[3] ? " (" + row[3] + ")" : "")]);

                }

            });

        } catch (e) { }

    };

    fetchExtra("เงินรับอื่นๆ", "เงินรับอื่นๆ");

    fetchExtra("เงินรับจากผู้สนับสนุน", "เงินรับจากผู้สนับสนุน");



    // 6. เรียงลำดับและคำนวณยอดคงเหลือ

    allData.sort((a, b) => a[0] - b[0]);

    let runningBalance = 0;

    let finalRows = allData.map(row => {

        runningBalance += (row[4] - row[3]);

        let exp = row[3] === 0 ? "" : row[3];

        let inc = row[4] === 0 ? "" : row[4];

        return [row[0], row[1], row[2], exp, inc, runningBalance, row[6], row[7]];

    });



    // 7. บันทึกลง Sheet Summary และ ตกแต่ง (Fixed Error Version)

    destSheet.clear();



    const headers = [["วันที่", "เวลา", "รายการ", "ถอนเงิน", "ฝากเงิน", "คงเหลือ", "กิจกรรม", "รายละเอียด"]];

    destSheet.getRange(1, 1, 1, 8).setValues(headers);



    if (finalRows.length > 0) {

        // ลงข้อมูล

        destSheet.getRange(2, 1, finalRows.length, 8).setValues(finalRows);



        // --- เริ่มส่วนตกแต่ง ---

        const fullRange = destSheet.getDataRange();

        const headerRange = destSheet.getRange(1, 1, 1, 8);

        const dataRange = destSheet.getRange(2, 1, finalRows.length, 8);



        // 7.1 Font & Size

        fullRange.setFontFamily("Sarabun").setVerticalAlignment("middle");

        fullRange.setFontSize(10);

        headerRange.setFontSize(11).setFontWeight("bold");



        // 7.2 Format Number & Date

        destSheet.getRange(2, 1, finalRows.length, 1).setNumberFormat("dd/MM/yy");

        destSheet.getRange(2, 4, finalRows.length, 3).setNumberFormat("#,##0.00;[Red]-#,##0.00;\"-\"");



        // 7.3 Alignment

        destSheet.getRange(2, 1, finalRows.length, 2).setHorizontalAlignment("center");

        destSheet.getRange(2, 4, finalRows.length, 3).setHorizontalAlignment("right");

        destSheet.getRange(2, 3, finalRows.length, 1).setHorizontalAlignment("left");

        destSheet.getRange(2, 7, finalRows.length, 2).setHorizontalAlignment("left");



        // 7.4 Header Style

        headerRange.setBackground("#1a237e")

            .setFontColor("#ffffff")

            .setHorizontalAlignment("center");



        // 7.5 Borders

        fullRange.setBorder(true, true, true, true, true, true, "#b0bec5", SpreadsheetApp.BorderStyle.SOLID);



        // 7.6 [แก้ไขใหม่] สีสลับบรรทัดแบบ Manual (แก้ Error: applyRowBanding)

        // วิธีนี้เสถียรกว่าการใช้ฟังก์ชันอัตโนมัติ

        let bgColors = [];

        for (let i = 0; i < finalRows.length; i++) {

            if (i % 2 !== 0) {

                // แถวคู่ (Index คี่) ให้เป็นสีฟ้าอ่อน

                bgColors.push(new Array(8).fill("#e8eaf6"));

            } else {

                // แถวคี่ (Index คู่) ให้เป็นสีขาว

                bgColors.push(new Array(8).fill("#ffffff"));

            }

        }

        // สั่งระบายสีทีเดียวทั้งตาราง

        dataRange.setBackgrounds(bgColors);



        // 7.7 Freeze & Resize

        destSheet.setFrozenRows(1);

        destSheet.autoResizeColumns(1, 8);

        if (destSheet.getColumnWidth(8) < 200) destSheet.setColumnWidth(8, 250);

    }



    return "อัปเดตข้อมูลและจัดรูปแบบตารางเรียบร้อยแล้ว";

}

