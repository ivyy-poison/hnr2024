import React, { useState } from 'react';
import { DatePicker, DatePickerValue } from "@tremor/react";

export default function Header() {
    const [selectedDate, setSelectedDate] = useState(new Date());

    const formatDate = (date: Date) => {
        return date.toLocaleDateString('en-US', { year: 'numeric', month: '2-digit', day: '2-digit' });
    }

    return (
        <div className="mt-10 flex flex-col items-center justify-center sm:mt-20">
          <div className="flex items-center text-2xl font-bold">
            <span className="w-full">Today's date is </span>
            <DatePicker className="ml-4 text-xl font-bold w-80" value={selectedDate} onValueChange={(newDate: DatePickerValue) => {
              if (newDate) {
                alert(`date is selected to ${newDate.toLocaleDateString()}`)
                setSelectedDate(newDate);
              }
            }} enableClear={false} />
          </div>
        </div>
    )
}