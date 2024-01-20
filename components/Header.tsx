import React, { useState } from 'react';
import { DatePicker, DatePickerValue } from "@tremor/react";

interface Props {
  date: Date;
  setDate: (date: Date) => void;
}

export default function Header({date, setDate}: Props) {
    return (
        <div className="mt-10 flex flex-col items-center justify-center sm:mt-20">
          <div className="flex items-center text-2xl font-bold">
            <span className="w-full">Today's date is </span>
            <DatePicker className="ml-4 text-xl font-bold w-80" value={date} onValueChange={(newDate: DatePickerValue) => {
              if (newDate) {
                setDate(newDate);
              }
            }} enableClear={false} />
          </div>
        </div>
    )
}