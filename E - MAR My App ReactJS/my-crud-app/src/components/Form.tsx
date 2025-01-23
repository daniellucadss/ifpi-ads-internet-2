// src/components/Form.tsx
import React, { useEffect } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';

interface FormProps {
  onSubmit: SubmitHandler<{ name: string }>;
  defaultValues?: { name: string };
}

const Form: React.FC<FormProps> = ({ onSubmit, defaultValues }) => {
  const { register, handleSubmit, reset, setValue } = useForm({ defaultValues });

  useEffect(() => {
    if (defaultValues) {
      setValue('name', defaultValues.name);
    }
  }, [defaultValues, setValue]);

  const submitHandler: SubmitHandler<{ name: string }> = data => {
    onSubmit(data);
    reset();
  };

  return (
    <form onSubmit={handleSubmit(submitHandler)}>
      <input {...register('name')} placeholder="Name" />
      <button type="submit">Submit</button>
    </form>
  );
};

export default Form;
