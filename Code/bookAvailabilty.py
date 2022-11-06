# book search using ISBN
def book_locator():
    bookISBN_list = [9780425268148, 9781643750255, 9780593136300, 9780385344142, 9780316735735, 9781728232744, 9781501173219, 9781250074133, 9781416590293, 9781616201340, 9781250167026, 9780385527156, 9781487503727, 9781250149060, 9781590515525, 9780062670847, 9780345470614, 9780865478015, 9781616206901, 9780345528681, 9781503215153, 9780385721790, 9780312358334, 9780486280615, 9780307455871,9780224097284, 9780307388995, 9781524763138, 9780062134578, 9781250002532, 9780698411616, 9780802117793, 9781742612829, 9781408800874, 9780241441510, 9780990694977, 9780316010733, 9780099468196, 9780241413210, 9780571276639, 9780743298858, 9780375842207, 9781594483295, 9781250014528, 9780525575238, 9780618593941, 9780312422912, 9781594634734, 9780425252963, 9780312305543, 9780062491794, 9780141040745, 9784130611268, 9780871407771, 9780007342600, 9781501134517, 9780393312836, 9780590557153, 9780099422686, 9781400034710, 9780060560379, 9780679603351, 9780670896769, 9789026349256, 9781908434425, 9780307408877, 9780307743725, 9780345533661, 9780340980934, 9781476798172, 9780099284826, 9780525949978, 9780307474278, 9780060740436, 9780375505294, 9780060957353, 9781786893253, 9781587888144, 9780385346856, 9781481463706, 9781984801487, 9780349142111, 9780460041515, 9780141439846, 9781250012579, 9780735220690, 9781250010124, 9781935554042, 9781501124389, 9780143127550, 9780061782213, 9780140186390, 9780062103222, 9781786486448, 9781473614444, 9780374909819, 9780199537150, 9781473676718, 9781492635222, 9780316260633, 9789036635769, 9780307588371, 9780066620992, 9781728228723, 9781476738918, 9780778308737, 9781524711764, 9780062285539, 9780399103421, 9780375707285, 9780375707285, 9781857990829, 9780062034601, 9781476799407, 9789401471947, 9789463413992, 9780312428549, 9781101971062, 9780062207517, 9781250005144, 9789021676272, 9780375703768, 9781503312753, 9780751554168, 9781250078407, 9780755331420, 9780385021746, 9780385486804, 9780385494786, 9781473217980, 9780670022458, 9780143038092, 9780812976731, 9781779502698, 9780545000109, 9781594631931, 9781473581739, 9781681195919, 9780743261982, 9781788169011, 9781786891686, 9781416589648, 9781509826582, 9780500251652, 9789026125690, 9780062914125, 9781101982266, 9781728215723, 9780316185905, 9780349142135, 9780448060194, 9780593332733, 9781402281945, 9780060518509, 9780143130154, 9780763680886, 9781476756554, 9780553418026, 9780393330342, 9780375704444, 9781400076093, 9789076542935, 9780241338322, 9780345441300, 9780141040080, 9781400078776, 9780061990625, 9780618485222, 9780307388971, 9780385537070, 9781250080400, 9780446520805, 9781481481731, 9781416954132, 9781447201809, 9780141197715, 9780393314366, 9780812996548, 9781416971719, 9789461740021, 9780140177398, 9780141377094, 9780743227445, 9780593101537, 9780307739513, 9780141439686, 9780141442464, 9781932416244, 9781611177220, 9781408418055, 9780307352156, 9781608198085, 9780316098335, 9780804165891, 9780307387899, 9780679781486, 9780312593315, 9780812985429, 9780545846608, 9780307700315, 9780393333091, 9781250207418, 9780142001745, 9780525656159, 97803853487135, 9781400096534, 9780062259318, 9781594485015, 9781250255617, 9781393248507, 9780500014981, 9781400033430, 9781473203280, 9780061769092, 9781596912939, 9789078641322, 9781594483851, 9781400033201, 9781420946888, 9780752881676, 9780316034005, 9780061984037, 9781400032808, 9780307947475, 9781416562603, 9781250130945, 9780307277183, 9780593191415, 9781542017022, 9780307720665, 9780141199085, 9781400078431, 9781635575361, 9781891729225]
    #print(len(bookISBN_list))

    def bookSearch(bookISBN_list, bookSearch_ISBN):
        for i in range (len(bookISBN_list)):
            if (bookISBN_list[i] == bookSearch_ISBN):
                return True
        return False

    # user input book ISBN
    while True:
        bookISBN = int(input("\nEnter Book ISBN:\t"))
        if not (bookSearch(bookISBN_list, bookISBN)):
            print("\nSorry, the book is unavailable in the library.")
            continue
        else:
            print("\nThe book is available in the library. \nDo you want to borrow this book?")
            break

book_locator()