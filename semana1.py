def descuentos(kilo):
    mandarina=1990
    total=kilo*mandarina

    if 0 < kilo <= 2:
        descuento=0.1*total
        descuentoFinal=total-descuento
        print(f"Total base   : {total}")
        print(f"descuento    : {descuento} (10%)")

    elif 2 < kilo <= 5:
        descuento=0.2*total
        descuentoFinal=total-descuento
        print(f"Total base   : {total}")
        print(f"descuento    : {descuento} (20%)")

    elif 5 < kilo <= 10:
        descuento=0.3*total
        descuentoFinal=total-descuento
        print(f"Total base   : {total}")
        print(f"descuento    : {descuento} (30%)")

    elif kilo > 10:
        descuento=0.4*total
        descuentoFinal=total-descuento
        print(f"Total base   : {total}")
        print(f"descuento    : {descuento} (40%)")

    else:
        print("Ingreso invalido")
        return None

    return descuentoFinal

################### INTERFAZ ##########################

print("******Compra de mandarinas******\n")
print("Precio de la mandarina $ 1990 el kilo\n")

kilos=float(input("Ingrese Numero de Kilos: "))
precioTotal=descuentos(kilos)

print(f"Total a pagar: {precioTotal}\n")
